#!/usr/bin/env python

REPORT = 100000
FS_SIZE = 70000000
FS_NEEDED = 30000000

tree = {}
stack = []
with open('./input.txt') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('$'):
            parts = line.split(' ')
            if len(parts) == 2:
                pass # ls follows
            elif len(parts) == 3:
                _, _, path = parts
                if path == '/':
                    stack.append(tree)
                elif path == '..':
                    stack.pop()
                else:
                    stack.append(stack[-1][path])
        elif line.startswith('dir'):
            _, path = line.split(' ')
            stack[-1][path] = {}
        else:
            size, path = line.split(' ')
            stack[-1][path] = int(size)

paths = {}
def walk(node, path):
    size = 0
    for k, v in node.items():
        size += walk(v, path + [k]) if isinstance(v, dict) else v
    paths['/'.join(path)] = size
    return size

walk(tree, [''])
reportable = { k: v for k, v in paths.items() if v <= REPORT }
total_reportable = sum(reportable.values())
print(f"total reportable: {total_reportable}")

left_to_free = FS_NEEDED - (FS_SIZE - paths[''])
candidates = { k: v for k, v in paths.items() if v >= left_to_free }
min_candidate = min(candidates.values())
print(f"min candidate: {min_candidate}")
