#!/usr/bin/env python
import json
from itertools import zip_longest, chain

#file = "./test.txt"
file = "./input.txt"
dividers = ([[2]], [[6]])
packets = [[]]
correct = []

with open(file) as f:
    for line in f:
        if line.strip() == '':
            packets.append([])
            continue
        packets[-1].append(json.loads(line))

def compare(l, r):
    if l is None: return True
    if r is None: return False
    if isinstance(l, int) and isinstance(r, int):
        if l == r: return None
        return l < r
    if isinstance(l, int): l = [l]
    if isinstance(r, int): r = [r]
    for _l, _r in zip_longest(l, r):
        res = compare(_l, _r)
        if res is None: continue
        return res

def bubble(arr):
    n = len(arr)
    swap = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if compare(arr[j+1], arr[j]): # looking for greater
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swap:
            return

for i, pair in enumerate(packets):
    left, right = pair
    if compare(left, right):
        correct.append(i + 1)

correct_sum = sum(correct)
print(f"correct sum: {correct_sum}")

flat = list(chain(*packets))
flat.extend(dividers)
bubble(flat)
first = flat.index(dividers[0])
second = flat.index(dividers[1], first)

decoder = (first+1)*(second+1)
print(f"decoder key: {decoder}")
