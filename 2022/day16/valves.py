#!/usr/bin/env python

import re
from collections import defaultdict
from dataclasses import dataclass, field
from math import inf

@dataclass
class Valve:
    id: str
    rate: int
    next: tuple[str]
    dist: defaultdict = field(default_factory=lambda:defaultdict(lambda:inf))
    def make_dist(self, valves):
        d = self.dist = defaultdict(lambda:inf)
        stack = [self.id]
        seen = set(stack)
        while stack:
            v = stack.pop(0)
            if v == self.id: d[v] = 0
            for u in filter(lambda u: u not in seen, valves[v].next):
                if d[u] > d[v] + 1: d[u] = d[v] + 1
                stack.append(u)
                seen.add(u)

p = re.compile(r"(?:rate=(\d+)|([A-Z]{2}))")
#file = "./test.txt"
file = "./input.txt"

start = 'AA'
valves = {}
with open(file) as f:
    for line in f:
        v, r, *n = [next(filter(None, m)) for m in p.findall(line)]
        valves[v] = Valve(v, int(r), n)

for v in valves.values(): v.make_dist(valves)

def traverse(time):
    pathes = defaultdict(lambda: -1)
    stack = [(start, 0, time, set())]
    while stack:
        v, af, t, vi = stack.pop(0)
        vo = valves[v]
        if pathes[frozenset(vi)] < af:
            pathes[frozenset(vi)] = af
        for n in filter(lambda n: n not in vi and vo.dist[n] < t and valves[n].rate > 0, vo.dist.keys()):
            nf = (t - vo.dist[n] - 1) * valves[n].rate
            stack.append((n, af + nf, t - vo.dist[n] - 1, vi | {n}))
    return pathes

solo = traverse(30)
print(f"solo, 30 minutes: {max(solo.values())}")

dual = traverse(26)
dual_best = max(f1 + f2 for p1, f1 in dual.items() for p2, f2 in dual.items() if not p1 & p2)
print(f"dual, 26 minutes: {dual_best}")
