#!/usr/bin/env python

max_cal = 0
cals = []

with open('./input.txt') as f:
    cal = 0
    for food in f:
        food = food.rstrip()
        if food == "":
            print(f"elf: {cal}")
            cals.append(cal)
            if cal > max_cal:
                max_cal = cal
            cal = 0
            continue
        cal += int(food.rstrip())

print(f"max: {max_cal}")

cals.sort(reverse=True)
top3 = sum(cals[:3])

print(f"top 3: {top3}")
