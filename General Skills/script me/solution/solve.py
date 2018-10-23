#!/usr/bin/python2
from pwn import *

# Function to find the maximum nesting depth of any round brackets expression
def max_depth(line):
    i, max = 0, 0
    for c in line:
        if c == '(':
            i+=1
        else:
            i-=1
        if i > max:
            max = i
    return max

r = remote('2018shell1.picoctf.com', 61344)
r.recvuntil('Example:')
r.recvlines(2)

for i in range(5):
    r.recvlines(2)
    problem = r.recvline()
    r.recvuntil('> ')

    # Get the question itself
    parts = problem.split(" = ")[0].split(" + ")

    ans = parts[0]
    for j in range(1, len(parts)):
        current = parts[j]
        
        # The rules are essentially are:
        #   if the two expressions have the same maximum depth concatenate them
        #   else, take the smallest one and insert it into the first level of the deeper one
        
        if max_depth(current) > max_depth(ans):
            ans = current[1]+ans+current[1:]
        elif max_depth(ans) > max_depth(current):
            ans = ans[:-1]+current+ans[-1]
        else:
            ans = ans + current

    r.sendline(ans)
    info("Problem: %s" % problem)
    info("Answer: %s" % ans)

    if 'Correct!' not in r.recvline():
        warning(r.recvall(timeout=1))
        break
    
    success("Correct!")

print(r.recv())