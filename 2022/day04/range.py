#!/usr/bin/env python

contains = 0
overlaps = 0
with open('./input.txt') as f:
    for line in f:
        ranges = []
        for s in line.rstrip().split(','):
            _min, _max = s.split('-')
            ranges.append(range(int(_min), int(_max)+1))
        left, right = ranges #sorted(ranges, key=min)
        if min(max(left), max(right)) - max(min(left), min(right)) >= 0:
            overlaps += 1
        if (min(left) in right and max(left) in right) or (min(right) in left and max(right) in left):
            contains += 1

print(f"contained: {contains}")
print(f"overlaps : {overlaps}")
