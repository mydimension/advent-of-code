#!/usr/bin/env python

import re
from itertools import chain
from collections import defaultdict

if False:
    file = "./test.txt"
    Y=10
    search = 20
else:
    file = "./input.txt"
    Y=2000000
    search=4000000

freq = lambda x, y: (x*4000000)+y

p = re.compile(r"x=(-?\d+), y=(-?\d+)")

beacons = defaultdict(set)
coverage = {}
with open(file) as f:
    for line in f:
        sx, sy, bx, by = [int(n) for n in chain.from_iterable(p.findall(line))]
        coverage[(sx, sy)] = abs(sx-bx) + abs(sy-by)
        beacons[by].add(bx)

def row_coverage(y):
    row = []
    for s, d in coverage.items():
        Ymin, Ymax = s[0] - (d - abs(y-s[1])), s[0] + (d - abs(y-s[1]))
        if Ymin <= Ymax:
            row.append([Ymin, Ymax])

    row.sort()
    merged = [row[0]]
    for c in row:
        prev = merged[-1]
        if c[0] <= prev[1] + 1:
            prev[1] = max(prev[1], c[1])
        else:
            merged.append(c)
    return merged

Ymerged = row_coverage(Y)
count = sum([abs((mmax+1) - mmin) for mmin, mmax in Ymerged])
for bx in beacons[Y]:
    for mmin, mmax in Ymerged:
        if mmin <= bx <= mmax:
            count -= 1
print(f"row({Y}): {count}")

found = None
for y in range(0, search+1):
    merged = row_coverage(y)
    if len(merged) == 1:
        continue
    if 0 <= merged[1][0] - 1 <= search:
        found = (merged[1][0] - 1, y)
        break

if found:
    print(f"found: {found}; frequency: {freq(*found)}")
