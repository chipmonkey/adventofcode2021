import re
from ventsday1 import vents
from vents import vents2

f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

print(values)

values = [re.split(' -> |,', x) for x in values]
values = [list(map(int, r)) for r in values]

print(values)


# Part 1
v = vents(values)
print(v.maxx)
print(v.maxy)

score = v.count_overlaps()

print(f"part 1: game: {score}")


# Part 2
v = vents2(values)

score = v.count_overlaps()

print(f"part2: game: {score}")
