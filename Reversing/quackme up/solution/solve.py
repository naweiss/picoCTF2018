#!/usr/bin/python2

# Note: rol and rot work in byte level
def ror(x, n):
    return (x >> n) | ((x << (8 - n)) & 0xff)

def rol(x, n):
    return ((x << n) & 0xff) | (x >> (8 - n))
    
def encrypt(text):
    ans = ''
    for c in text:
        tmp = rol(ord(c), 4)
        tmp = tmp^0x16
        tmp = ror(tmp, 8)
        ans += chr(tmp)
    return ans

def decrypt(text):
    ans = ''
    for c in text:
        tmp = rol(ord(c), 8)
        tmp = tmp^0x16
        tmp = ror(tmp, 4)
        ans += chr(tmp)
    return ans
    
def hexify(text):
    return " ".join("{:02x}".format(ord(c)) for c in text)

if __name__ == "__main__":
    assert(encrypt(decrypt("ABCD")) == "ABCD")
    
    ans = decrypt("\x11\x80\x20\xE0\x22\x53\x72\xA1\x01\x41\x55\x20\xA0\xC0\x25\xE3\x95\x20\x15\x35\x20\x15\x00\x70\xC1")
    
    print(hexify(ans))
    print(ans)