#!/usr/bin/env python

""" Actual:
    X: loose
    Y: draw
    Z: win

    Rock(1) < Paper(2) < Scissors(3) < Rock(1)
"""

def score(them, me):
    if them == me:
        return 3
    if {1,3} == {them,me}:
        return 6 if me == 1 else 0
    if them < me:
        return 6
    return 0

def should_pick(them, me):
    them += me - 2
    if them == 4: return 1
    if them == 0: return 3
    return them

total = 0
real_total = 0
with open('./input.txt') as f:
    for line in f:
        them, me = line.rstrip().split(' ')

        T = ord(them) - 64
        M = ord(me) - 64 - 23

        total += M + score(T, M)
        real_total += should_pick(T, M) + score(T, should_pick(T, M))

print(f"total: {total}")
print(f"real : {real_total}")
