import sys
import re

class Shop:
    def __init__(self, filename):
        self.filename = filename
        self.products = {}
        self.customers = {}

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("Product:"):
                        product_info = line.split(":")[1].strip().split(",")
                        product_name, product_quantity = product_info[0], int(product_info[1])
                        self.products[product_name] = product_quantity
                    elif line.startswith("Customer:"):
                        customer_name = line.split(":")[1].strip()
                        self.customers[customer_name] = {}

        except FileNotFoundError:
            print("File not found. Make sure the file exists.")
            sys.exit(1)

    def warehouse(self):
        print("Warehouse:")
        print("-------------+------------")
        print("Nazwa towaru | Ilość sztuk")
        print("-------------+------------")
        for product, quantity in self.products.items():
            print(f"{product.ljust(13)}{quantity}")
        print()

    def sell(self, command):
        customers_data = command.split()
        for i in range(1, len(customers_data)):
            customer_and_products = customers_data[i].split(":")
            customer_name = customer_and_products[0]
            products = customer_and_products[1].split(",")
            customer_dict = self.customers.get(customer_name)
            if customer_dict is None:
                print(f"Customer '{customer_name}' not found.")
                continue

            for product_info in products:
                product_name, quantity = product_info.split("(")
                product_name = product_name.strip()
                quantity = int(quantity[:-1])
                if product_name not in self.products:
                    print(f"Product '{product_name}' does not exist in the warehouse.")
                elif self.products[product_name] < quantity:
                    print(f"Not enough '{product_name}' in the warehouse for customer '{customer_name}'.")
                elif quantity < 0:
                    print(f"Cannot sell negative quantity of '{product_name}' to customer '{customer_name}'.")
                else:
                    customer_dict[product_name] = customer_dict.get(product_name, 0) + quantity
                    self.products[product_name] -= quantity

    def show(self, command):
        customers_data = command.split()
        for i in range(1, len(customers_data)):
            customer_name = customers_data[i]
            customer_dict = self.customers.get(customer_name)
            if customer_dict is None:
                print(f"Customer '{customer_name}' not found.")
            else:
                print(f"{customer_name}:")
                print("-------------+------------")
                print("Nazwa towaru | Ilość sztuk")
                print("-------------+------------")
                for product, quantity in customer_dict.items():
                    print(f"{product.ljust(13)}{quantity}")
                print()

    def process_commands(self):
        while True:
            try:
                command = input("> ")
                if not command:
                    continue
                elif command == "warehouse":
                    self.warehouse()
                elif command.startswith("sell"):
                    self.sell(command)
                elif command.startswith("show"):
                    self.show(command)
                else:
                    print("Unknown command.")
            except EOFError:
                break

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: sklep.py [filename]")
        sys.exit(1)

    filename = sys.argv[1]
    shop = Shop(filename)
    shop.load_data()
    shop.process_commands()
