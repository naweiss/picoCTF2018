#!/usr/bin/python2
from pwn import *

def ror_2(x, n):
    return (x >> n) | ((x << (16 - n)) & 0xffff)

def rol_2(x, n):
    return ((x << n) & 0xffff) | (x >> (16 - n))

def ror_4(x, n):
    return (x >> n) | ((x << (32 - n)) & 0xffffffff)

def rol_4(x, n):
    return ((x << n) & 0xffffffff) | (x >> (32 - n))

def encrypt(password):
    password = list(password)
    
    for i in range(len(password)-3):
        password[i] = chr(ord(password[i]) ^ 0x9d)
        
        ans = ror_2(u16(''.join(password[i:i+2])), 5)
        password[i:i+2] = p16(ans)
        
        ans = rol_4(u32(''.join(password[i:i+4])), 11)
        password[i:i+4] = p32(ans)
    
    return ''.join(password)
    
def decrypt(password):
    password = list(password)
    
    for i in reversed(range(len(password)-3)):
        num = ror_4(u32(''.join(password[i:i+4])), 11)
        password[i:i+4] = p32(num)
        
        num = rol_2(u16(''.join(password[i:i+2])), 5)
        password[i:i+2] = p16(num)
        
        password[i] = chr(ord(password[i]) ^ 0x9d)
    
    return ''.join(password)
        
if __name__ == "__main__":
    expected = "7b18a636da3b2ba6fecb82ae96ff9f468f36a7affe938e3f46a7ff82cfceb397171aa736ef2b8aed"
    print(decrypt(expected.decode("hex")))