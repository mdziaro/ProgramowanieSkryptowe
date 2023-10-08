import sys


def display(args,show_index):
    for i in range(len(args)):
        if show_index == "True":
            print("args[%d] = " %i, end="")
        print(args[i])
    return 0

if __name__ == "__main__":
    show_index=sys.argv[1]
    args=sys.argv[2:]
    if not (show_index == "True" or show_index == "False"):
        print("Set first argument as \"True\" or \"False\"")
        exit(1)
    print("System wystartował.")
    display(args, show_index)
    print("System zakończył działanie.")
    exit(0)