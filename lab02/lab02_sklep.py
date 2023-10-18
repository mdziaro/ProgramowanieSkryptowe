import sys


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"Plik {file_name} nie istnieje.")
        sys.exit(1)


def display_warehouse(data):
    lines = data.strip().split('\n')
    print("--------------+------------ ")
    print(lines[0])  # Nazwa | Ilosc
    print("--------------+------------ ")
    for line in lines[1:]:
        print(line)


def display_customer_purchases(data, customers):
    for customer in customers:
        print(customer)
        lines = data.get(customer, '')
        if not lines:
            continue
        lines = lines.strip().split('\n')
        print("--------------+------------ ")
        print(lines[0])  # Klient
        print("--------------+------------ ")
        print(lines[1])  # Nazwa | Ilosc
        for line in lines[2:]:
            print(line)
        print("\n")



def process_sell_command(data, sell_command):
    sell_parts = sell_command.split()
    if len(sell_parts) % 2 != 0:
        print("Niepoprawny format komendy")
        return

    for i in range(0, len(sell_parts), 2):
        customer = sell_parts[i]
        purchases = sell_parts[i + 1]
        purchases = purchases.split(':')
        customer_data = data.get(customer, '')
        customer_lines = customer_data.strip().split('\n')
        for purchase in purchases:
            product, quantity = purchase.split('(')
            product = product.strip()
            quantity = int(quantity[:-1].strip())
            for j in range(2, len(customer_lines)):
                parts = customer_lines[j].split()
                if parts[0] == product:
                    available_quantity = int(parts[1])
                    if available_quantity >= quantity:
                        customer_lines[j] = f"{product:<13}{available_quantity - quantity}"
                    else:
                        print(f"{product} - nie ma takiego towaru")
            data[customer] = "\n".join(customer_lines)            


def main(file_name):
    data = load_data(file_name)
    lines = data.strip().split('\n')
    warehouse_data = {}
    customer_data = {}
    current_customer = None

    for line in lines[2:]:
        if not line:
            current_customer = None
        elif current_customer:
            customer_data[current_customer] += '\n' + line
        else:
            parts = line.split()
            if len(parts) == 2:
                product, quantity = parts
                warehouse_data[product] = int(quantity)
            elif len(parts) == 1:
                current_customer = parts[0]
                customer_data[current_customer] = ''

    while True:
        try:
            command = input("> ")
            if not command:
                continue
        except EOFError:  # Obsługa Ctrl+D (Linux, macOS) / Ctrl+Z Enter (Windows)
            break

        command_parts = command.split()
        if command_parts[0] == "warehouse":
            display_warehouse(data)
        elif command_parts[0] == "show":
            customers_to_show = command_parts[1:]
            display_customer_purchases(customer_data, customers_to_show)
        elif command_parts[0] == "sell":
            process_sell_command(customer_data, command)
        else:
            print("Nieznana komenda")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: sklep.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    main(file_name)
