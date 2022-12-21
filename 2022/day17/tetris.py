#!/usr/bin/env python

from itertools import cycle, zip_longest
from functools import cache

#file = "./test.txt"
file = "./input.txt"

rock, wind = None, None

def setup():
    global rock
    global wind
    # shapes are inverted: bottom to top
    rock = cycle([
        [0b0011110],
        [0b0001000,
        0b0011100,
        0b0001000],
        [0b0011100,
        0b0000100,
        0b0000100],
        [0b0010000,
        0b0010000,
        0b0010000,
        0b0010000],
        [0b0011000,
        0b0011000],
    ])

    with open(file) as f:
        wind = cycle(f.readline().strip())

@cache
def play(n, t=tuple()):
    h = 0
    for _ in range(n):
        t, dh = drop(t)
        h += dh
    return (t, h)

@cache
def drop(t):
    r = tuple([0] * len(t) + [0,0,0] + next(rock))

    done = False
    while not done:
        r, done = step(t, r)

    nt = tuple([ tl | rl for tl, rl in zip_longest(t, r, fillvalue=0)])
    return nt[-40:], len(nt) - len(t)

@cache
def step(t, r):
    w = next(wind)

    s, b = (int.__rshift__, 0b0000001) if w == ">" else (int.__lshift__, 0b1000000)
    if not any(l & b for l in r) and not any((s(rl, 1)) & tl for rl, tl in zip(r, t)):
        r = tuple((s(l, 1) for l in r))

    if any(tl & rl for tl, rl in zip_longest([0b1111111] + list(t), r, fillvalue=0)) or r[0]:
        return r, True

    return r[1:], False

setup()

_, height = play(2022)
print(f"height after 2022: {height}")

setup()

total = 1_000_000_000_000
chunk = 100_000
tower = tuple()
height = 0
for _ in range(int(total/chunk)):
    tower, dh = play(chunk, tower)
    height += dh
print(f"height after {total}: {height}")
