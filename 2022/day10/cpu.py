#!/usr/bin/env perl

from itertools import count

X = 1 # sprite pos
clock = count(1) # draw pixel pos
probes = { 20: None, 60: None, 100: None, 140: None, 180: None, 220: None }
screen = ''

def exe(cmd, arg=None):
    global X
    if cmd == 'noop':
        yield next(clock)
    elif cmd == 'addx':
        yield next(clock)
        yield next(clock)
        X += int(arg)

with open('./input.txt') as f:
#with open('./test.txt') as f:
    for line in f:
        for c in exe(*line.rstrip().split(' ')):
            if c in probes:
                probes[c] = X
            sprite = range(X, X+3)
            screen += '#' if c%40 in sprite else '.'
            if c%40 == 0:
                screen += "\n"

print(probes)
print(sum([k*v for k, v in probes.items()]))

print(screen)
