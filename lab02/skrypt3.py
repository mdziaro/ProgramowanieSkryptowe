#!/usr/bin/env python3

import argparse
import operations
import sys

def main():
    parser = argparse.ArgumentParser(description="Script to process text data.")
    subparsers = parser.add_subparsers(dest="command", help="Choose a command to execute")

    # skrypt1.py
    skrypt1_parser = subparsers.add_parser("skrypt1")
    skrypt1_parser.add_argument("text", help="Text to process")

    # skrypt2.py 
    skrypt2_parser = subparsers.add_parser("skrypt2")
    skrypt2_subparsers = skrypt2_parser.add_subparsers(dest="subcommand", help="Choose 'cut' or 'grep' command")

    # cut flags
    cut_parser = skrypt2_subparsers.add_parser("cut")
    cut_parser.add_argument("-d", "--delimiter", required=True, help="Delimiter for 'cut' command")
    cut_parser.add_argument("-f", "--field", type=int, required=True, help="Field for 'cut' command")

    # grep flags
    grep_parser = skrypt2_subparsers.add_parser("grep")
    grep_parser.add_argument("pattern", help="Pattern to search for")
    grep_parser.add_argument("-i", "--ignore-case", action="store_true", help="Ignore case when searching")
    grep_parser.add_argument("-w", "--whole-words", action="store_true", help="Search for whole words only")

    args = parser.parse_args()

    if args.command == "skrypt1":
        process_skrypt1(args.text)
    elif args.command == "skrypt2":
        if args.subcommand == "cut":
            process_cut(args)
        elif args.subcommand == "grep":
            process_grep(args)
        else:
            print("Unrecognized subcommand. Use 'cut' or 'grep'.")

def process_skrypt1(text):
    for func_name in dir(operations):
        if callable(getattr(operations, func_name)):
            func = getattr(operations, func_name)
            result = func(text)
            print(result)

def process_cut(args):
    import cut
    input_text = sys.stdin.read()
    lines = input_text.split('\n')
    for line in lines:
        result = cut.cut(line, args.delimiter, args.field)
        print(result)

def process_grep(args):
    import grep
    input_text = sys.stdin.read()
    result = grep.grep(args.pattern, input_text, args.ignore_case, args.whole_words)
    print(result)

if __name__ == "__main__":
    main()
