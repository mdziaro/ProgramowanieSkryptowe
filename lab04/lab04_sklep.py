import pickle
from datetime import date

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Produkt: {self.name}\nIlość: {self.quantity}\nCena: {self.price} zł"


class Client:
    id_counter = 1  # Licznik do nadawania unikalnych ID klientom

    def __init__(self, surname, name):
        self.id = Client.id_counter
        Client.id_counter += 1
        self.surname = surname
        self.name = name
        self.basket = []

    def buy(self, product, quantity):
        if product in Store.products:
            if product.quantity >= quantity:
                if quantity > 0:
                    product.quantity -= quantity
                    self.basket.append((product, quantity))
                    print(f"{self.name} bought {quantity} {product.name}")
                else:
                    print(f"Błąd: Nie można sprzedawać ujemnej ilości produktów.")
            else:
                print(f"Błąd: Liczba dostępnych sztuk w magazynie to {product.quantity}")
        else:
            print(f"Błąd: Produkt {product.name} nie został znaleziony w magazynie.")

    def calculate_total(self):
        total_value = sum(product.price * quantity for product, quantity in self.basket)
        return total_value

    def __str__(self):
        return f"{self.id}. {self.surname} {self.name}\n" + "\n".join(
            [f"Produkt: {product.name}, Ilość: {quantity}" for product, quantity in self.basket]
        ) + f"\nWartość zakupionych produktów wynosi {self.calculate_total()} zł"


class Transaction:
    def __init__(self, client, product, date):
        self.client = client
        self.product = product
        self.date = date


class Store:
    products = [Product("Komputer", 20, 2000), Product("Laptop", 15, 5000)]
    transactions = []
    FILENAME = "store_data.pkl"

    @classmethod
    def sell_product(cls, client_id, product_index, quantity):
        client = next((c for c in list_of_clients if c.id == client_id), None)
        product = Store.products[product_index]

        if client is None:
            client = Client("Nowy", "Klient")
            list_of_clients.append(client)

        client.buy(product, quantity)
        transaction = Transaction(client, product, date.today())
        cls.transactions.append(transaction)

    @classmethod
    def display_transactions_by_client_id(cls, client_id):
        client = next((c for c in list_of_clients if c.id == client_id), None)

        if client is not None:
            client_transactions = [t for t in cls.transactions if t.client == client]
            grouped_transactions = {}
            for transaction in client_transactions:
                if transaction.date not in grouped_transactions:
                    grouped_transactions[transaction.date] = []

                grouped_transactions[transaction.date].append(transaction.product)

            for date, products in grouped_transactions.items():
                total_value = sum(product.price for product in products)
                print(f"Data: {date}, Suma wartości: {total_value} zł, Kupione produkty: {', '.join(p.name for p in products)}")
        else:
            print(f"Klient o ID {client_id} nie istnieje.")

    @classmethod
    def add_product(cls):
        try:
            name = input("Podaj nazwę produktu: ")

            # Sprawdzenie, czy nazwa produktu jest unikalna
            if any(product.name.lower() == name.lower() for product in cls.products):
                raise ValueError("Błąd: Produkt o podanej nazwie już istnieje.")

            quantity = int(input("Podaj ilość produktu: "))
            if quantity < 0:
                raise ValueError("Błąd: Ilość produktu nie może być ujemna.")

            price = float(input("Podaj cenę produktu: "))
            if price < 0:
                raise ValueError("Błąd: Cena produktu nie może być ujemna.")

            new_product = Product(name, quantity, price)
            cls.products.append(new_product)

            print(f"Dodano nowy produkt: {new_product}")

        except ValueError as e:
            print(e)

    @classmethod
    def load_data(cls):
        try:
            with open(cls.FILENAME, "rb") as file:
                data = pickle.load(file)

            cls.products = [Product(p['name'], p['quantity'], p['price']) for p in data['products']]
            
            # Zmieniłem sposób wczytywania danych dotyczących transakcji
            cls.transactions = [Transaction(Client(p['client']['surname'], p['client']['name']),
                                            Product(p['product']['name'], p['product']['quantity'], p['product']['price']),
                                            date.fromisoformat(p['date']))
                                for p in data['transactions']]

        except (FileNotFoundError, pickle.UnpicklingError):
            print("Błąd podczas wczytywania danych.")

    @classmethod
    def save_data(cls):
        data = {
            'products': [{'name': p.name, 'quantity': p.quantity, 'price': p.price} for p in cls.products],
            'transactions': [{'client': {'surname': t.client.surname, 'name': t.client.name},
                               'product': {'name': t.product.name, 'quantity': t.product.quantity, 'price': t.product.price},
                               'date': t.date.isoformat()}
                              for t in cls.transactions]
        }

        with open(cls.FILENAME, "wb") as file:
            pickle.dump(data, file)

# Utwórz listę klientów
list_of_clients = [Client("Kowalski", "Jan"), Client("Nowak", "Anna")]

# Przy założeniu, że chcesz wczytać dane z pliku na początku programu:
Store.load_data()

while True:
    try:
        command = input("Komenda: ")
        if command == "warehouse":
            print([product.name for product in Store.products])
        elif command == "clients":
            print([f"{client.id}. {client.surname} {client.name}" for client in list_of_clients])
        elif command.startswith("show"):
            parts = command.split()
            if len(parts) == 2:
                client_id = int(parts[1])
                if any(client.id == client_id for client in list_of_clients):
                    Store.display_transactions_by_client_id(client_id)
                else:
                    print("Błąd: Nieprawidłowy ID klienta.")
            else:
                print("Błąd: Nieprawidłowa komenda.")
        elif command.startswith("sell"):
            parts = command.split()
            if len(parts) >= 4:
                client_id = int(parts[1])
                product_index = int(parts[2])
                quantity = int(parts[3])
                if any(client.id == client_id for client in list_of_clients) and 0 <= product_index < len(
                        Store.products):
                    Store.sell_product(client_id, product_index, quantity)
                else:
                    print("Błąd: Nieprawidłowy ID klienta lub indeks produktu.")
            else:
                print("Błąd: Nieprawidłowa komenda.")
        elif command.startswith("warehouse"):
            parts = command.split()
            if len(parts) == 2:
                product_index = int(parts[1])
                if 0 <= product_index < len(Store.products):
                    print(Store.products[product_index])
                else:
                    print("Błąd: Nieprawidłowy indeks produktu w magazynie.")
            else:
                print("Błąd: Nieprawidłowa komenda.")
        elif command.lower() == "add":
            Store.add_product()
        elif command.lower() == "exit":
            # Zakończ program
            break
        else:
            print("Nieznana komenda.")
    except (EOFError, KeyboardInterrupt):
        # Na zakończenie programu zapisz dane do pliku:
        Store.save_data()
        break