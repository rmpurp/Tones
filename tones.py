#!/usr/bin/env python3

import pyperclip
import readline
import argparse

# Constants
vowels = ['a', 'e', 'i', 'o', 'u', 'v']
first = ['ā', 'ē', 'ī', 'ō', 'ū','ǖ']
second = ['á', 'é', 'í', 'ó', 'ú', 'ǘ']
third = ['ǎ', 'ě', 'ǐ', 'ǒ', 'ǔ', 'ǚ']
fourth = ['à', 'è', 'ì', 'ò', 'ù', 'ǜ']

to_first = dict(zip(vowels, first))
to_second = dict(zip(vowels, second))
to_third = dict(zip(vowels, third))
to_forth = dict(zip(vowels, fourth))

tone_dict = dict(zip(range(1, 5), (to_first, to_second, to_third, to_forth)))

vowel_priority = ['a', 'o', 'e', 'ui', 'i', 'u', 'v'] 

def replace_vowel(buf, tone):
    reversed = buf[::-1]
    v = get_vowels(reversed)
    
    for letter in vowel_priority:
        if letter in v:
            if letter == 'ui':
                letter = 'u'
            return reversed.replace(letter, tone_dict[tone][letter], 1)[::-1]
    # Some sort of error
    return buf
          
def get_vowels(reversed):
    found_vowel = False
    v = ''
    for letter in reversed:
        if letter in vowels:
            v += letter
            found_vowel = True
        elif found_vowel:
            break
    return v

def process_text(text):
    buffer = ''
    result = ''
    replacing_mode = False
    escape_mode = False
    for letter in text:
        if letter == '\\':
            if escape_mode:
                buffer += '\\'
            escape_mode = not escape_mode
            replacing_mode = False
        elif letter.isdigit():
            tone = int(letter)
            if not(replacing_mode) or escape_mode:
                buffer += letter
            elif 1 <= tone <= 4:
                result += replace_vowel(buffer, tone)
                buffer = ''
                replacing_mode = False
            elif tone not in (0, 5):
                buffer += letter
                replacing_mode = False
        elif letter.isalpha():
            replacing_mode = True 
            escape_mode = False
            buffer += letter
        else: #Symbol
            buffer += letter 
            replacing_mode = False
            escape_mode = False
    return result + buffer

def repl():
    while True:
        try:
            text = input('~-> ')
            result = process_text(text) 
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
            print(process_text(line.strip()))


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
