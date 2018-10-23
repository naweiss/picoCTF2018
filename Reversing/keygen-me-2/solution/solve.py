
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def order(char):
    return alphabet.index(char)

def check_passworder(key):
    if len(key) < 2: return True
    if (order(key[0])+order(key[1])) % 36 != 14: return False
    
    if len(key) < 3: return True
    if (order(key[2])-order(key[0])) % 36 != 6: return False
    
    
    if len(key) < 4: return True
    if (order(key[2])+order(key[3])) % 36 != 24: return False
    
    if len(key) < 6: return True
    if (order(key[1])+order(key[3])+order(key[5])) % 36 != 4: return False
    if (order(key[3])+order(key[4])+order(key[5])) % 36 != 22: return False
    
    if len(key) < 7: return True
    if (order(key[2])+order(key[4])+order(key[6])) % 36 != 13: return False
    
    if len(key) < 8: return True
    if (order(key[1])+order(key[4])+order(key[7])) % 36 != 7: return False
    
    if len(key) < 11: return True
    if (order(key[6])+order(key[8])+order(key[10])) % 36 != 31: return False
    if (order(key[8])+order(key[9])+order(key[10])) % 36 != 27: return False
    
    if len(key) < 14: return True
    if (order(key[7])+order(key[12])+order(key[13])) % 36 != 23: return False
    
    if len(key) < 16: return True
    if (order(key[9])+order(key[12])+order(key[15])) % 36 != 20: return False
    if (order(key[13])+order(key[14])+order(key[15])) % 36 != 12: return False
    
    return True
    
def key_gen(passed = ""):
    if check_passworder(passed):
        if len(passed) == 16:
            print(passed)
        else:
            for char in alphabet:
                key_gen(passed+char)
            
if __name__ == "__main__":
    key_gen()