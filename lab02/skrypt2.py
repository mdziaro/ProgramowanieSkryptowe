import sys
import cut
import grep

def main():
    if len(sys.argv) < 2:
        print("Podaj komendę cut lub grep.")
        return

    command = sys.argv[1]

    if command == "cut":
        if len(sys.argv) != 6 or sys.argv[2] != "-d" or sys.argv[4] != "-f":
            print("Użycie: ./skrypt2.py cut -d <delimiter> -f <field>")
            return
        
        delimiter = sys.argv[3]
        field = int(sys.argv[5])

        input_text = sys.stdin.read()
        lines = input_text.split('\n')
        for line in lines:
            result = cut.cut(line, delimiter, field)
            print(result)

    elif command == 'grep':
        pattern = sys.argv[-1]
        input_text = sys.stdin.read()
        ignore_case = '-i' in sys.argv
        whole_words = '-w' in sys.argv

        result = grep.grep(pattern, input_text, ignore_case, whole_words)
        print(result)

    else:
        print("Nierozpoznana komenda. Użyj 'cut' lub 'grep'.")

if __name__ == "__main__":
    main()
