#!/usr/bin/env python3

from datetime import date
import json

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

class Store:
    products = [
        Product("Komputer", 10, 2000),
        Product("Laptop", 20, 5000),
        # Dodaj więcej produktów według potrzeb
    ]
    services = [
        Service("Instalacja oprogramowania", 100),
        Service("Konfiguracja sieci", 150),
        # Dodaj więcej usług według potrzeb
    ]

    clients = {}

    @classmethod
    def add_product(cls, name, quantity, price):
        product = Product(name, quantity, price)
        cls.products.append(product)

    @classmethod
    def add_service(cls, name, price):
        service = Service(name, price)
        cls.services.append(service)

    @classmethod
    def sell_product(cls, first_name, last_name, item_index, quantity):
        client = cls.get_or_create_client(first_name, last_name)

        product = cls.products[item_index]

        if quantity <= product.quantity:
            transaction = Transaction(client, product, date.today(), quantity)
            client.buy(product, quantity, date.today())
            return transaction
        else:
            print(f"Błąd: Liczba dostępnych sztuk w magazynie to {product.quantity}")
            return None

    @classmethod
    def sell_service(cls, first_name, last_name, service_index):
        client = cls.get_or_create_client(first_name, last_name)

        service = cls.services[service_index]
        transaction = Transaction(client, service, date.today(), 1)
        client.buy(service, 1, date.today())
        return transaction

    @classmethod
    def show_client_transactions(cls, first_name, last_name):
        client = cls.clients.get((first_name, last_name))
        if client is not None:
            client.show_transactions()

    @classmethod
    def get_or_create_client(cls, first_name, last_name):
        client_key = (first_name, last_name)
        client = cls.clients.get(client_key)
        if client is None:
            client = Client(first_name, last_name)
            cls.clients[client_key] = client
        return client
    
    

    @classmethod
    def serialize(cls):
        data = {
            'products': [{'name': p.name, 'quantity': p.quantity, 'price': p.price} for p in cls.products],
            'services': [{'name': s.name, 'price': s.price} for s in cls.services],
            'clients': {}
        }

        for (first_name, last_name), client in cls.clients.items():
            data['clients'][(first_name, last_name)] = {
                'transactions': {}
            }

            for product_name, transactions in client.transactions.items():
                data['clients'][(first_name, last_name)]['transactions'][product_name] = [{
                    'date': t.date.isoformat(),
                    'quantity': t.quantity
                } for t in transactions]

        return json.dumps(data)

    @classmethod
    def deserialize(cls, data):
        data = json.loads(data)

        cls.products = [Product(p['name'], p['quantity'], p['price']) for p in data['products']]
        cls.services = [Service(s['name'], s['price']) for s in data['services']]
        cls.clients = {}

        for (first_name, last_name), client_data in data['clients'].items():
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

    def buy(self, product_or_service, quantity, date):
        if product_or_service.name not in self.transactions:
            self.transactions[product_or_service.name] = []

        transaction = Transaction(self, product_or_service, date, quantity)
        self.transactions[product_or_service.name].append(transaction)

        if isinstance(product_or_service, Product):
            product_or_service.quantity -= quantity

    def show_transactions(self):
        print(f"{self.first_name} {self.last_name}:")
        for product_name, transactions in self.transactions.items():
            total_quantity = sum([t.quantity for t in transactions])
            total_value = sum([t.quantity * t.product_or_service.price for t in transactions])
            print(f"Data: {transactions[0].date}, Produkt/Usługa: {product_name}, Ilość: {total_quantity}, Wartość: {total_value} zł")

# Obsługa poleceń z wejścia standardowego
while True:
    try:
        command = input("> ").split()
        if not command:
            continue
        elif command[0] == "warehouse":
            print("Magazyn:")
            for i, product in enumerate(Store.products):
                print(f"{i}. {product}")
            for i, service in enumerate(Store.services):
                print(f"{i + len(Store.products)}. {service}")
        elif command[0] == "clients":
            for (first_name, last_name), client in Store.clients.items():
                print(f"{first_name} {last_name}")
        elif command[0] == "show":
            first_name = command[1]
            last_name = command[2]
            Store.show_client_transactions(first_name, last_name)
        elif command[0] == "sell":
            first_name = command[1]
            last_name = command[2]
            item_index = int(command[3])
            quantity = int(command[4])
            if item_index < len(Store.products):
                transaction = Store.sell_product(first_name, last_name, item_index, quantity)
                if transaction:
                    print(f"Sprzedano produkt {transaction.product_or_service.name} \nCena: {transaction.product_or_service.price}\nCena razem: {transaction.product_or_service.price*quantity} \nIlość: {quantity}\ndo klienta: {first_name} {last_name}")
            else:
                service_index = item_index - len(Store.products)
                transaction = Store.sell_service(first_name, last_name, service_index)
                if transaction:
                    print(f"Sprzedano usługę {transaction.product_or_service.name} \nCena: {transaction.product_or_service.price}\nCena razem: {transaction.product_or_service.price*quantity} \nIlość: {quantity}\ndo klienta: {first_name} {last_name}")

        else:
            print("Nieznane polecenie.")
    except EOFError:
        break
