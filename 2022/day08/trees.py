#!/usr/bin/env python

def rindex(li, x):
    return next(i for i in reversed(range(len(li))) if li[i] == x)

forest = []
with open('./input.txt') as f:
    for line in f:
        forest.append([ int(t) for t in line.rstrip() ])

visible = 0
vis_score = 0
for y, row in enumerate(forest):
    for x, t in enumerate(row):
        w, e, n, s = (
            row[:x],                    row[x+1:],
            [r[x] for r in forest[:y]], [r[x] for r in forest[y+1:]] )

        wm, em, nm, sm = [max(m, default=-1) for m in (w,e,n,s)]

        visible += sum([1 if any([wm < t, em < t, nm < t, sm < t]) else 0])

        wm, em, nm, sm = [max(m, t) for m in (wm,em,nm,sm)]

        wv, ev, nv, sv = (
                (len(w) - rindex(w, wm) if wm in w else len(w)),
                (e.index(em)+1          if em in e else len(e)),
                (len(n) - rindex(n, nm) if nm in n else len(n)),
                (s.index(sm)+1          if sm in s else len(s)),)

        vis_score = max(vis_score, wv*ev*nv*sv)

print(f"total visible: {visible}")
print(f"vis score:     {vis_score}")
