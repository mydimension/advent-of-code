#!/usr/bin/env python

from dataclasses import dataclass

#file = "./test.txt"
file = "./input.txt"

@dataclass
class Node:
    pos: list[int]
    height: int
    g: int = 0
    h: int = 0
    prev: "Node" = None

    @property
    def f(self): return self.g + self.h

    def __eq__(self, other): return self.pos == other.pos

    def steps(self):
        n = self
        while n.prev:
            yield n.pos
            n = n.prev

    def reset(self):
        self.g = 0
        self.h = 0
        self.prev = None

def astar(maze, start, end):
    open_set = [maze[start[1]][start[0]]]
    closed_set = []

    while open_set:
        current = sorted(open_set, key=lambda x:x.f)[0]
        if current.pos == end:
            return current

        open_set = list(filter(lambda x:x != current, open_set))
        closed_set.append(current)
        for move in ((1,0),(-1,0),(0,1),(0,-1)):
            x, y = move
            neighbor = [current.pos[0] + x, current.pos[1] + y]
            if min(neighbor) < 0: continue
            if neighbor[0] >= len(maze[0]) or neighbor[1] >= len(maze): continue
            neighbor = maze[neighbor[1]][neighbor[0]]
            if neighbor in closed_set or neighbor.height > current.height + 1: continue

            found = False
            g = current.g + 1
            for o in open_set:
                if neighbor == o:
                    if g < o.g:
                        o.g = g
                        o.h = abs(o.pos[0] - end[0]) + abs(o.pos[1] - end[0])
                        o.prev = current
                    found = True
            if not found:
                neighbor.g = g
                neighbor.h = abs(neighbor.pos[0] - end[0]) + abs(neighbor.pos[1] - end[1])
                neighbor.prev = current
                open_set.append(neighbor)

def reset(maze):
    for row in maze:
        for cell in row:
            cell.reset()

start = []
end = []

maze = []
with open(file) as f:
    for line in f:
        row = []
        for cell in line.rstrip():
            if cell == 'S':
                cell = 'a'
                start = [len(row), len(maze)]
            if cell == 'E':
                cell = 'z'
                end = [len(row), len(maze)]
            row.append(Node([len(row), len(maze)], ord(cell) - ord('a')))
        maze.append(row)

cand = {}
for row in maze:
    for cell in row:
        if cell.height != 0: continue
        good = False
        for move in ((1,0),(-1,0),(0,1),(0,-1)):
            x, y = move
            neighbor = [cell.pos[0] + x, cell.pos[1] + y]
            if min(neighbor) < 0: continue
            if neighbor[0] >= len(maze[0]) or neighbor[1] >= len(maze): continue
            neighbor = maze[neighbor[1]][neighbor[0]]
            if neighbor.height != cell.height + 1: continue
            good = True
            break
        if not good: continue

        reset(maze) # probably a better way to reuse results, but eh...
        final = astar(maze, cell.pos, end)
        if final:
            cand[tuple(cell.pos)] = len(list(final.steps()))

part1 = cand[tuple(start)]
part2 = min(cand.values())
print(f"Part 1: {part1}; Part 2: {part2}")
