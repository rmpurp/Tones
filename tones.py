#!/usr/bin/env python3

import pyperclip
import readline
import argparse
import tone_process as tp

def repl():
    while True:
        try:
            text = input('~-> ')
            result = tp.convert(text) 
            print(result)
            pyperclip.copy(result)
        except KeyboardInterrupt:
            print()
        except EOFError:
            print()
            exit()

def process_file(file_name):
    with open(file_name) as f:
        for line in f:
            print(tp.convert(line.strip()))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs='?', type=str,
            help='file name to be parsed', default="")
    args = parser.parse_args()
    return vars(args)["filename"]

def main():
    file_name = parse_args()
    if file_name:
        process_file(file_name)
    else:
        repl()

if __name__ == '__main__':
    main()
