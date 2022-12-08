#!/usr/bin/env python
from collections import deque

stacks = []
CrateMover = 9001

with open('./input.txt') as f:
    # init stacks
    for line in f:
        line = line.rstrip()
        if line == '':
            break
        if '[' not in line:
            continue

        for i, cargo in enumerate([line[j+1:j+2] for j in range(0, len(line), 4)]):
            if len(stacks) <= i:
                stacks.insert(i, deque())
            if cargo == ' ':
                continue
            stacks[i].appendleft(cargo)

    # process movements
    for line in f:
        _, n, _, i, _, j = line.rstrip().split(' ')
        from_s, to_s = stacks[int(i) - 1], stacks[int(j) - 1]
        if CrateMover == 9000:
            for _ in range(int(n)):
                to_s.append(from_s.pop())
        elif CrateMover == 9001:
            to_s.extend(reversed([from_s.pop() for _ in range(int(n))]))

print(''.join([s[-1] for s in stacks]))
