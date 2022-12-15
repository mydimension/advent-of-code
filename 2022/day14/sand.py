#!/usr/bin/env python
from collections import defaultdict
from itertools import tee, chain
from math import inf

#file = "./test.txt"
file = "./input.txt"

def pairwise(iterable): # doing this on python3.9, 3.10 got official pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

rocks = defaultdict(set)
sand = defaultdict(set)
origin = (500, 0)
with open(file) as f:
    for line in f:
        rock = []
        for pairs in line.strip().split(' -> '):
            rock.append([int(n) for n in pairs.split(',')])
        for a, b in pairwise(rock):
            if a[0] == b[0]:
                _min, _max = sorted([a[1],b[1]])
                for n in range(_min, _max+1):
                    rocks[a[0]].add(n)
            if a[1] == b[1]:
                _min, _max = sorted([a[0],b[0]])
                for n in range(_min, _max+1):
                    rocks[n].add(a[1])

def drop(col, row, floor=inf):
    bottom = min(filter(lambda x:x>=row, rocks[col]|sand[col]|{floor}))
    if bottom is inf or bottom == 0: return False
    for n in (col-1, col+1):
        if bottom not in filter(lambda x:x>=row, rocks[n]|sand[n]|{floor}):
            return drop(n, bottom, floor=floor)
    sand[col].add(bottom-1)
    return True

# part 1
while drop(*origin): pass

print(sum([len(s) for s in sand.values()]))

floor = max(chain.from_iterable([list(s) for s in rocks.values()])) + 2
print(f"floor: {floor}")

# part 2
while drop(*origin, floor=floor): pass

print(sum([len(s) for s in sand.values()]))
