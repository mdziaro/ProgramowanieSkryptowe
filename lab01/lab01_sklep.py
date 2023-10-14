import json
import sys

def check_if_negative(stan, ilosc_sprzedana):
    if stan - ilosc_sprzedana < 0:
        print("Sprzedaż niemożliwa, za mało produktów na stanie")
        return False
    return True

def sell_wares(data, rodzaj, ilosc_sprzedana):
    for item in data:
        if item["nazwa"] == rodzaj:
            if check_if_negative(item["liczba"], ilosc_sprzedana):
                item["liczba"] = item["liczba"] - ilosc_sprzedana
                return item["liczba"]
            else:
                break
    else:
        print(f"Produkt '{rodzaj}' nie istnieje w magazynie lub nie ma go na stanie.")

if __name__ == "__main__":
    with open(r'C:\Users\student42\Desktop\lab01\magazyn.json', 'r') as file:
        data = json.load(file)
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == "--stan_magazynu":
            for item in data:
                print(f"{item['nazwa']}: {item['liczba']}")
        elif sys.argv[i].isalpha() and i + 1 < len(sys.argv) and sys.argv[i + 1].isnumeric():
            if sys.argv[i+1]<0:
                print("nie mozna sprzedac ujemnej wartosci.")
                break
            rodzaj = sys.argv[i]
            ilosc_sprzedana = int(sys.argv[i + 1])
            sell_wares(data, rodzaj, ilosc_sprzedana)

    with open(r'C:\Users\student42\Desktop\lab01\magazyn.json', 'w') as file:
        json.dump(data, file)
