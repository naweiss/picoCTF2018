#!/usr/bin/python2
from pwn import *

r = remote('2018shell1.picoctf.com', 15853)
r.recvuntil('Please give me the ')
binary_word = r.recvuntil(' as a word.', drop=True)

word = ""
for char in binary_word.split(' '):
    word += chr(int(char, 2))
r.sendline(word)

r.recvuntil('Please give me the ')
hex_word = r.recvuntil(' as a word.', drop=True)

r.sendline(hex_word.decode('hex'))

r.recvuntil('Please give me the  ')
octal_word = r.recvuntil(' as a word.', drop=True)

word = ""
for char in octal_word.split(' '):
    word += chr(int(char, 8))
r.sendline(word)

r.recvuntil('Flag: ')
print(r.recvall())