#!/usr/bin/python3

# This is a Vigenere Cipher
# There are tools online to solve this problem but I wrote my own

matrix = []
alphabet = ''

# Filling the matrix and setting the alphabet
# You can skip that part
with open('../table.txt') as table:
    lines = table.read().splitlines()
    
    header = lines[0]
    alphabet = header.replace(' ', '')

    # Skip the first 2 lines and the last line
    for line in lines[2:-1]:
        # get row's content
        line = line.split('|')[1]
        row = line.split(' ')[1:]
        matrix.append(row)

# Find character's index in the alphabet
def find(alphabet, char):
    return alphabet.index(char.upper())

if __name__ == "__main__":
    msg = "llkjmlmpadkkc"
    key = "thisisalilkey"

    res = ""
    for i in range(len(key)):
        x = find(alphabet, key[i])
        y = find(matrix[x], msg[i])
        res += alphabet[y]
    
    print(res)