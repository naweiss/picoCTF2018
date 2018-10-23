from z3 import *

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__ == "__main__":
    s =  Solver()
    
    vec, length = "", 16
    for i in range(length):
        vec += "key[{}] ".format(i)
    # Note: extra space at the end adds to m another empty array value
    m = BitVecs(vec, 8)
    
    for i in range(length):
        s.add(And(m[i] >= 0, m[i] < len(alphabet)))
    
    s.add((m[0] + m[1]) % 36 == 14)
    s.add((m[2] - m[0]) % 36 == 6)
    s.add((m[2] + m[3]) % 36 == 24)
    s.add((m[1] + m[3] + m[5]) % 36 == 4)
    s.add((m[3] + m[4] + m[5]) % 36 == 22)
    s.add((m[2] + m[4] + m[6]) % 36 == 13)
    s.add((m[1] + m[4] + m[7]) % 36 == 7)
    s.add((m[6] + m[8] + m[10]) % 36 == 31)
    s.add((m[8] + m[9] + m[10]) % 36 == 27)
    s.add((m[7] + m[12] + m[13]) % 36 == 23)
    s.add((m[9] + m[12] + m[15]) % 36 == 20)
    s.add((m[13] + m[14] + m[15]) % 36 == 12)
    
    while s.check() == z3.sat:
        model = s.model()
        # Note: the -1 is used to ignore the empty array value
        model_chars = [alphabet[model[i].as_long()] for i in m[:-1]]
        print(''.join(model_chars))
        
        # prevent next model from using the same assignment as a previous model
        s.add(Or([i != model[i] for i in m[:-1]]))