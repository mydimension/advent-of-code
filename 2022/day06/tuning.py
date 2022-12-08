#!/usr/bin/env python
from collections import Counter

PACKET = 4
MESSAGE = 14
MODE = MESSAGE - 1

with open('./input.txt') as f:
    line = f.readline().rstrip()
    c = Counter(line[:MODE])
    for i in range(MODE, len(line)):
        c.update(line[i])
        if len(+c) == MODE + 1:
            i += 1 # report 1-based index
            print(f"done: {i}")
            break
        c.subtract(line[i-MODE])
