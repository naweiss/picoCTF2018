from z3 import *
import sys

# Use the same verification on the z3 special variables
def calc_verify(key_bits, gates):
    b = [i for i in key_bits]
    # Do all the calculation
    for name, args in gates:
        if name == 'true':
            b.append(1)
        else:
            u1 = b[args[0][0]] ^ args[0][1]
            u2 = b[args[1][0]] ^ args[1][1]
            if name == 'or':
                b.append(u1 | u2)
            elif name == 'xor':
                b.append(u1 ^ u2)
    return b

def findKey(chalbox):
    length, gates, check = chalbox
    
    # Reversed binary form of key
    vec = ""
    for i in reversed(range(length)):
        vec += "key[{}] ".format(i)
    
    # Note: the extra space at the end adds to key another empty array value
    key = BitVecs(vec, 1)
    # Note: the -1 is used to ignore the empty array value
    b = calc_verify(key[:-1], gates)
    
    # Add constraints
    s =  Solver()
    s.add(b[check[0]] ^ check[1] == True)
    
    # Get solution
    assert (s.check() == z3.sat)
    model = s.model()
    
    # convert key to string bits and the binary string
    # Note: the -1 is used to ignore the empty array value
    model_bits = [model[i].as_string() for i in key[:-1]]
    model_binary = ''.join(reversed(model_bits))
    # convert to a number
    return int(model_binary, 2)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <map.txt>'
        exit(1)
    
    with open(sys.argv[1], 'r') as f:
        cipher, chalbox = eval(f.read())

    key = findKey(chalbox)
    # Find the smallest value possible
    assert (key < (1 << chalbox[0]))
    
    print(key)