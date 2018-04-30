import pyperclip
import readline


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

letter_priority = ['a', 'o', 'e', 'ui' , 'i', 'u', 'v'] 

def replace_vowel(buf, tone):
    reversed = buf[::-1]
    v = get_vowels(reversed)
    
    for letter in letter_priority:
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

while True:
    try:
        text = input('~-> ')
     
        buffer = ''
        result = ''
        for letter in text:
            if letter.isdigit():
                tone = int(letter)
                if 1 <= tone <= 4:
                    result += replace_vowel(buffer, tone)
                    buffer = ''
            else:
                buffer += letter 
        result += buffer
        print(result)
        pyperclip.copy(result)
    except KeyboardInterrupt:
        print()
    except EOFError:
        print()
        exit()
