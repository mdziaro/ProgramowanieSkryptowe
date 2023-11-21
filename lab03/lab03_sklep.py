class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Produkt: {self.name}\nIlość: {self.quantity}\nCena: {self.price} zł"

class Client:
    def __init__(self, name):
        self.name = name
        self.basket = []

    def buy(self, product, quantity):
        if product in list_of_products_in_warehouse:
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
        return f"{self.name}\n" + "\n".join([f"Produkt: {product.name}, Ilość: {quantity}" for product, quantity in self.basket]) + f"\nWartość zakupionych produktów wynosi {self.calculate_total()} zł"

# Hardcodowana lista produktów
list_of_products_in_warehouse = [Product("Komputer", 7, 2000), Product("Laptop", 15, 5000)]

# Hardcodowana lista klientów
list_of_clients = [Client("Jan Kowalski"), Client("Anna Nowak")]

while True:
    try:
        command = input("Komenda: ")
        if command == "warehouse":
            print([product.name for product in list_of_products_in_warehouse])
        elif command == "clients":
            print([client.name for client in list_of_clients])
        elif command.startswith("show"):
            parts = command.split()
            if len(parts) == 2:
                client_index = int(parts[1])
                if 0 <= client_index < len(list_of_clients):
                    print(list_of_clients[client_index])
                else:
                    print("Błąd: Nieprawidłowy indeks klienta.")
            else:
                print("Błąd: Nieprawidłowa komenda.")
        elif command.startswith("sell"):
            parts = command.split()
            if len(parts) >= 4:
                client_index = int(parts[1])
                product_index = int(parts[2])
                quantity = int(parts[3])
                if 0 <= client_index < len(list_of_clients) and 0 <= product_index < len(list_of_products_in_warehouse):
                    client = list_of_clients[client_index]
                    product = list_of_products_in_warehouse[product_index]
                    client.buy(product, quantity)
                else:
                    print("Błąd: Nieprawidłowy indeks klienta lub produktu.")
            else:
                print("Błąd: Nieprawidłowa komenda.")
        elif command.startswith("warehouse"):
            parts = command.split()
            if len(parts) == 2:
                product_index = int(parts[1])
                if 0 <= product_index < len(list_of_products_in_warehouse):
                    print(list_of_products_in_warehouse[product_index])
                else:
                    print("Błąd: Nieprawidłowy indeks produktu w magazynie.")
            else:
                print("Błąd: Nieprawidłowa komenda.")
        else:
            print("Nieznana komenda.")
    except EOFError:
        break