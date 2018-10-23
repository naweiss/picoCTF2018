#!/usr/bin/python2
HEADER_SIZE = 54

with open('../pico2018-special-logo.bmp','r') as img:
    # skip the bmp header
    data = img.read()[HEADER_SIZE:]
    
    # get the LSB from every byte
    bits = ''.join([str(ord(byte) & 1) for byte in data])
    
    # convert the bit-stream back to bytes
    ans = ""
    for i in range(0, len(bits), 8):
        ans += chr(int(bits[i : i+8], 2))
    print(ans)
    
    print("Note: scroll up")