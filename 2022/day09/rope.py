#!/usr/bin/env python

rope = [[0,0] for _ in range(10)]
visited = set()
visited.add(tuple(rope[-1]))

def move_tail(d, l, r, cb=None):
    xy = 1 if d in ('U', 'D') else 0
    st = 1 if d in ('R', 'U') else -1
    for _ in range(l):
        h = r[0]
        h[xy] += st
        for t in r[1:]:
            if all([abs(h[j] - t[j]) <= 1 for j in (0,1)]):
                break
            if h[0] == t[0]:
                t[1] += 1 if h[1] > t[1] else -1
            elif h[1] == t[1]:
                t[0] += 1 if h[0] > t[0] else -1
            else:
                t[0] += 1 if h[0] > t[0] else -1
                t[1] += 1 if h[1] > t[1] else -1
            h = t
        cb(r[-1])

with open('./input.txt') as f:
    for line in f:
        direction, distance = line.rstrip().split(' ')

        move_tail(direction, int(distance), rope, lambda t:visited.add(tuple(t)))

total_visited = len(visited)
print(f"visited: {total_visited}")
