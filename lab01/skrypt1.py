import sys

descriptions = {'f': "Zwierzak idzie do przodu", 'b':"Zwierzak idzie do tyłu", 'l':"Zwierzak skręca w lewo", 'r':"Zwierzak skręca w prawo"}

def display(args,show_index):
    for i in range(len(args)):
        if show_index == "True":
            print("args[%d] = " %i, end="")
        print(args[i])
    return 0


def run(moves, move_descriptions):
    for i in moves:
        if i in move_descriptions:
            print(move_descriptions[i])
               

if __name__ == "__main__":
    show_index=sys.argv[1]
    args=sys.argv[2:]
    if not (show_index == "True" or show_index == "False"):
        print("Set first argument as \"True\" or \"False\"")
        exit(1)
    print("System wystartował.")
    print("Funkcja pierwsza:\nStart")
    display(args, show_index)
    print("Stop")
    if show_index == "False":
        print("Funkcja druga:\nStart")
        run(args, descriptions)
        print("Stop")
    print("System zakończył działanie.")
    exit(0)