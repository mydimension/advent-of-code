#!/usr/bin/env python

def priority(items):
    return sum([ord(ch) - (38 if ch.isupper() else 96) for ch in items])

group = []
badge_priority = 0
total_priority = 0
with open('./input.txt') as f:
    for line in f:
        line = line.rstrip()
        mid = int(len(line)/2)
        left, right = set(line[:mid]), set(line[mid:])
        total_priority += priority(left & right)

        group.append(set(line))
        if len(group) == 3:
            badge = group[0].intersection(*group[1:])
            badge_priority += priority(badge)
            #print(badge, priority(badge))
            group = []

print(f"priority sum: {total_priority}")
print(f"badge priority: {badge_priority}")
