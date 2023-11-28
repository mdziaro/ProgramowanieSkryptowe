from datetime import date
import json
import logging
import sys

logging.basicConfig(filename='store_logs.log', level=logging.INFO)

class AccessError(Exception):
    pass


def admin(func):
    def wrapper(*args, **kwargs):
        is_admin = (sys.argv[2][:6]=="admin_")
        if not is_admin:
            raise AccessError("Tylko administratorzy mogą wywoływać tę funkcję.")
        return func(*args, **kwargs)
    return wrapper

def user(func):
    def wrapper(*args, **kwargs):
        user_name = sys.argv[2] if len(sys.argv) > 2 else None
        user_instance = args[0]

        if user_instance:
            class_name = getattr(user_instance, '__name__', user_instance.__class__.__name__)
            method_name = func.__name__
            logging.info(f"{date.today()}: Użytkownik {user_name} wywołał metodę {method_name} klasy {class_name}")
        return func(*args, **kwargs)

    if isinstance(func, classmethod):
        return classmethod(wrapper)
    else:
        return wrapper

class ProductOrServiceBase:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'"{self.name}"'

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}\nCena: {self.price}"

class Product(ProductOrServiceBase):
    def __init__(self, name, quantity, price):
        super().__init__(name, price)
        self.quantity = quantity

    def __str__(self):
        return f"{super().__str__()}\nIlość: {self.quantity}"

class Service(ProductOrServiceBase):
    pass

class Transaction:
    def __init__(self, client, product_or_service, date, quantity):
        self.client = client
        self.product_or_service = product_or_service
        self.date = date
        self.quantity = quantity

class Client:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.transactions = {}

    @user
    def buy(self, product_or_service, quantity, date):
        if product_or_service.name not in self.transactions:
            self.transactions[product_or_service.name] = []

        transaction = Transaction(self, product_or_service, date, quantity)
        self.transactions[product_or_service.name].append(transaction)

        if isinstance(product_or_service, Product):
            product_or_service.quantity -= quantity

    @user
    def show_transactions(self):
        print(f"{self.first_name} {self.last_name}:")
        for product_name, transactions in self.transactions.items():
            total_quantity = sum([t.quantity for t in transactions])
            total_value = sum([t.quantity * t.product_or_service.price for t in transactions])
            print(f"Data: {transactions[0].date}, Produkt/Usługa: {product_name}, Ilość: {total_quantity}, Wartość: {total_value} zł")

class Store:
    products = [
        Product("Komputer", 10, 2000),
        Product("Laptop", 20, 5000),
    ]
    services = [
        Service("Instalacja oprogramowania", 100),
        Service("Konfiguracja sieci", 150),
    ]

    clients = {}

    @classmethod
    @admin
    def add_new_product(cls, name, quantity, price):
        existing_product = next((p for p in cls.products if p.name == name), None)
        if existing_product is not None:
            print(f"Błąd: Produkt o nazwie {name} już istnieje")
        else:
            product = Product(name, quantity, price)
            cls.products.append(product)

    @classmethod
    @admin
    def add_new_service(cls, name, price):
        service = Service(name, price)
        cls.services.append(service)

    @classmethod
    @user
    def sell_product(cls, first_name, last_name, item_index, quantity):
        client = cls.get_or_create_client(first_name, last_name)

        if 0 <= item_index < len(cls.products):
            product = cls.products[item_index]

            if quantity <= product.quantity:
                transaction = Transaction(client, product, date.today(), quantity)
                client.buy(product, quantity, date.today())
                return transaction
            else:
                print(f"Błąd: Liczba dostępnych sztuk w magazynie to {product.quantity}")
                return None
        else:
            print("Błąd: Nieprawidłowy indeks produktu")
            return None

    @classmethod
    @user
    def sell_service(cls, first_name, last_name, service_index):
        client = cls.get_or_create_client(first_name, last_name)

        if 0 <= service_index < len(cls.services):
            service = cls.services[service_index]
            transaction = Transaction(client, service, date.today(), 1)
            client.buy(service, 1, date.today())
            return transaction
        else:
            print("Błąd: Nieprawidłowy indeks usługi")
            return None

    @classmethod
    @user
    def show_client_transactions(cls, first_name, last_name):
        client = cls.clients.get((first_name, last_name))
        if client is not None:
            client.show_transactions()

    @classmethod
    @user
    def get_or_create_client(cls, first_name, last_name):
        client_key = (first_name, last_name)
        client = cls.clients.get(client_key)
        if client is None:
            client = Client(first_name, last_name)
            cls.clients[client_key] = client
        return client

    @classmethod
    def serialize(cls, filename='store_data.json'):
        data = {
            'products': [{'name': p.name, 'quantity': p.quantity, 'price': p.price} for p in cls.products],
            'services': [{'name': s.name, 'price': s.price} for s in cls.services],
            'clients': {}
        }

        for (first_name, last_name), client in cls.clients.items():
            # Convert the key to a string
            client_key = f"{first_name} {last_name}"
            data['clients'][client_key] = {
                'transactions': {}
            }

            for product_name, transactions in client.transactions.items():
                data['clients'][client_key]['transactions'][product_name] = [{
                    'date': t.date.isoformat(),
                    'quantity': t.quantity
                } for t in transactions]

        with open(filename, 'w') as file:
            json.dump(data, file)


    @classmethod
    def deserialize(cls, filename='store_data.json'):
        with open(filename, 'r') as file:
            data = json.load(file)

        cls.products = [Product(p['name'], p['quantity'], p['price']) for p in data['products']]
        cls.services = [Service(s['name'], s['price']) for s in data['services']]
        cls.clients = {}

        for client_name, client_data in data['clients'].items():
            # Split the client name into first and last name
            first_name, last_name = client_name.split()

            client = Client(first_name, last_name)
            cls.clients[(first_name, last_name)] = client

            for product_name, transactions_data in client_data['transactions'].items():
                product = next((p for p in cls.products if p.name == product_name), None)
                service = next((s for s in cls.services if s.name == product_name), None)

                if product is not None:
                    transactions = [Transaction(client, product, date.fromisoformat(t['date']), t['quantity'])
                                    for t in transactions_data]
                    client.transactions[product_name] = transactions
                elif service is not None:
                    transactions = [Transaction(client, service, date.fromisoformat(t['date']), t['quantity'])
                                    for t in transactions_data]
                    client.transactions[product_name] = transactions


if __name__ == "__main__":
    file=sys.argv[1]
    Store.deserialize(file)
    try:
        while True:
            command = input("Podaj komendę (add, show, clients, warehouse, sell, add_client): ").strip().lower()

            if command == "add":
                user_input = input("Podaj dane (nazwa ilość cena lub nazwa cena): ").split()

                if len(user_input) == 3:
                    Store.add_new_product(user_input[0], int(user_input[1]), float(user_input[2]))
                elif len(user_input) == 2:
                    Store.add_new_service(user_input[0], float(user_input[1]))
                else:
                    print("Błąd: Nieprawidłowe dane")

            elif command == "show":
                user_input = input("Podaj dane (klient): ")
                first_name, last_name = user_input.split()
                Store.show_client_transactions(first_name, last_name)

            elif command == "clients":
                print("Lista klientów:")
                for (first_name, last_name), _ in Store.clients.items():
                    print(f"{first_name} {last_name}")

            elif command == "warehouse":
                print("Stan magazynu:")
                for product in Store.products:
                    print(f"{product.name} (Produkt): {product.quantity} sztuk Cena: {product.price}")
                for service in Store.services:
                    print(f"{service.name} (Usługa): Cena: {service.price} zł")

            elif command == "sell":
                user_input = input("Podaj dane (klient indeks ilosci): ").split(maxsplit=2)
                if len(user_input) == 3:
                    first_name, last_name, rest = user_input
                    try:
                        item_index, quantity = map(int, rest.split())
                        transaction = Store.sell_product(first_name, last_name, item_index, quantity)
                        if transaction:
                            product_or_service = transaction.product_or_service
                            total_value = quantity * product_or_service.price
                            print(f"Sprzedano {product_or_service.__class__.__name__} {product_or_service.name} klientowi {first_name} {last_name} o {quantity} sztukach. Łączna wartość: {total_value} zł")
                        else:
                            print("Transakcja nieudana.")
                    except ValueError:
                        print("Błąd: Nieprawidłowe dane")
                else:
                    print("Błąd: Nieprawidłowe dane")

            elif command == "add_client":
                user_input = input("Podaj dane klienta (imię nazwisko): ").split()
                if len(user_input) == 2:
                    first_name, last_name = user_input
                    Store.get_or_create_client(first_name, last_name)
                    print(f"Klient {first_name} {last_name} dodany.")
                else:
                    print("Błąd: Nieprawidłowe dane klienta")

            elif command == "exit":
                        Store.serialize(file)
                        break    
            else:
                print("Nieprawidłowa komenda. Dostępne komendy: add, show, clients, warehouse, sell")

            
    except AccessError as e:
        print(f"Błąd dostępu: {e}")