#!/usr/bin/python2
from random import randint
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ord(char):
    return alphabet.index(char)
    
def CRC(string):
    sum = 0
    for i in range(len(string)):
        sum += (i+1)*(ord(string[i])+1)
    
    # Note: apparently this is the same as sum - 36*floor(sum/36)
    #   Don't ask me why
    return sum - 4*9*(((sum * 0x38E38E39) >> 32) / 8)
    
def get_random_character():
    return alphabet[randint(0, len(alphabet) - 1)]

if __name__ == "__main__":
    first_15_chars = ""
    for i in range(15):
        first_15_chars += get_random_character()

    val = CRC(first_15_chars)
    last_char = alphabet[val]
    
    print(first_15_chars+last_char)
