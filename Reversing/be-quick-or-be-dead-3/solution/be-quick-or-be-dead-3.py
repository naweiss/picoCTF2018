MAX_INT = 0xffffffff

def calc(x):
    calculated = {}
    for i in range(x+1):
        # check here
        calculated[i] = _calc(i, calculated) % 0xffffffff 
    return calculated[x]

def _calc(x, calculated):
    if x < 5:
        return x**2+0x2345
    x_1 = calculated[x-1]
    x_2 = calculated[x-2]
    x_3 = calculated[x-3]
    x_4 = calculated[x-4]
    x_5 = calculated[x-5]
    return (x_1-x_2)+(x_3-x_4)+(x_5*0x1234)
    
if __name__ == "__main__":
    print(calc(0x186B5))