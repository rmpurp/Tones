# Tones
  A program that allows easy conversion from numbered tones to proper diacritics in Chinese Pinyin. Currently offers a REPL that allows input of a sentence to be converted, whose output is printed to the terminal and copied to the clipboard, as well as file input conversion.

# Operation
Operation requires Python 3 installed. Run using ```python3 tones.py [filename]```. If there are no file provided, then a REPL is opened that prompts the user for input and then prints the output and copying it to the clipboard. Input is Chinese Pinyin with tones indicated directly following the syllable with a number between 0 and 5. Neutral tone can be indicated using 0, 5, or nothing. 

## Handling of Digits
To be recognized as a tone number, the number must directly follow the syllable with no symbol separating the last letter and the number. Digits that are unambiguously not a tone number are added verbatim to the output. These situations are:
 * The digit is directly preceeded by another digit (including tone numbers)
 * The digit is directly preceeded by a symbol digit
 * The number is escaped (using ```\```)
     * To type ```\```, you must escape it by writing ```\\```.

# Dependencies
 * Requires Pyperclip for copying sentence to clipboard.
