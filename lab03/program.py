import sys
from controller import OptionsParser
from model import MoveDirection

descriptions = {
    MoveDirection.FORWARD: "Zwierzak idzie do przodu",
    MoveDirection.BACKWARD: "Zwierzak idzie do tyłu",
    MoveDirection.LEFT: "Zwierzak skręca w lewo",
    MoveDirection.RIGHT: "Zwierzak skręca w prawo"
}

def display(args, show_index):
    for i in range(len(args)):
        if show_index == "True":
            print(f"args[{i}] = {args[i]}")
    return 0

def run(moves, move_descriptions):
    for move in moves:
        if move in move_descriptions:
            print(move_descriptions[move])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python program.py <show_index> <move1> <move2> ...")
        exit(1)

    show_index = sys.argv[1]
    args = sys.argv[2:]
    if show_index not in ["True", "False"]:
        print("Set first argument as 'True' or 'False'")
        exit(1)

    if show_index == "False":
        display(args, show_index)
    
    print("System wystartował.")
    
    move_args = OptionsParser.parse(args)
    
    for i, arg in enumerate(args):
        if i < len(move_args):
            move = move_args[i]
            if move in MoveDirection:  # Sprawdź, czy kierunek istnieje w enumie
                if show_index == "True":
                    print(f"{i + 1}: {arg}")
                print(f"{descriptions[move]}")

    
    print("System zakończył działanie.")
    exit(0)
