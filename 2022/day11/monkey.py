#!/usr/bin/env python

#file = "./test.txt"
file = "./input.txt"
gcm = 1 # not strictly GCM, but good enough for this
if False:
    # part 1
    rounds = 20
    relief = 3
else:
    # part 2
    rounds = 10000
    relief = 1

monkeys = []
with open(file) as f:
    for line in f:
        line = line.strip()
        if line == '': continue

        if line.startswith('Monkey'):
            monkeys.append({'inspected': 0})
            continue

        if line.startswith('Starting items:'):
            _, _, items = line.partition(': ')
            monkeys[-1]['items'] = [int(x) for x in items.split(', ')]
            continue

        if line.startswith('Operation:'):
            _, _, expr = line.partition(' = ')
            monkeys[-1]['worry'] = eval(f"lambda old: {expr}") # Very Un-Safe!!!
            continue

        if line.startswith('Test:'):
            _, _, mod = line.rpartition(' ')
            monkeys[-1]['mod'] = int(mod)
            gcm *= int(mod)
            continue

        if line.startswith('If true:') or line.startswith('If false:'):
            mod_bool = line[ line.index(' ')+1 : line.index(':') ]
            _, _, to_monkey = line.rpartition(' ')
            monkeys[-1][f"mod_{mod_bool}"] = int(to_monkey)
            continue

for _ in range(rounds):
    for monkey in monkeys:
        while monkey['items']:
            monkey['inspected'] += 1
            item = monkey['items'].pop(0) # pop-left
            item = monkey['worry'](item)
            if relief > 1:
                item //= relief
            else:
                item %= gcm
            monkeys[ monkey['mod_true'] if item % monkey['mod'] == 0 else monkey['mod_false'] ]['items'].append(item)

top_0, top_1, *_ = sorted(monkeys, key=lambda x:x['inspected'], reverse=True)
business = top_0['inspected'] * top_1['inspected']
print(f"monkey business: {business}")
