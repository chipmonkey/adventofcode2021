from submarine import submarine
from sub2 import sub2

f = open('input.txt', 'r')
values = []
for line in f:
    values.append(line.strip())


# Part 1
sub = submarine()

for v in values:
    sub.move(v)

print(f"part 1: hpos: {sub.hpos} depth: {sub.depth} answer: {sub.hpos * sub.depth}")



# Part 2
sub2 = sub2()
for v in values:
    sub2.move(v)

print(f"part 2: hpos: {sub2.hpos} depth: {sub2.depth} aim: {sub2.aim} answer: {sub2.hpos * sub2.depth}")
