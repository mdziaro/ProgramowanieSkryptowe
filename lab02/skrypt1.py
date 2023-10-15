import sys
import operations 

def main():
    if len(sys.argv) != 2:
        print("Podaj dokładnie jeden argument - tekst do przetworzenia.")
        return

    text = sys.argv[1]

    # Iteracja po każdej funkcji z modułu operations (Alfabetycznie)
    for func_name in dir(operations):
        if callable(getattr(operations, func_name)):
            func = getattr(operations, func_name)
            result = func(text)
            print(result)

if __name__ == "__main__":
    main()