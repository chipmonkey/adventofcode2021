import copy
import itertools
from math import prod
from pandas import DataFrame

f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

maxx = len(values)

values = [[i for i in x] for x in values]
values = [list(map(int, x)) for x in values]

maxy = len(values[0])

flashes = 0

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1),
        (-1, -1), (-1, 1), (1, 1), (1, -1)]

def dezero(state):
    for x in range(maxx):
        for y in range(maxy):
            if state[x][y] > 9:
                state[x][y] = 0
    return state

def perform_flash(state, x, y):
    global flashes
    flashes = flashes + 1
    for dir in dirs:
        newx = x + dir[0]
        newy = y + dir[1]
        state = perform_addone(state, newx, newy)
    return state

def perform_addone(state, x, y):
    if x < 0 or y < 0 or x >= maxx or y >= maxy:
        return state
    state[x][y] = state[x][y] + 1
    if state[x][y] ==  10:
        state = perform_flash(state, x, y)
    return state

def runstep(state):
    for x in range(maxx):
        for y in range(maxy):
            state = perform_addone(state, x, y)
    state = dezero(state)
    return state

# Part 1

state = copy.deepcopy(values)
print("Before any steps:")
print(DataFrame(state))
for i in range(100):
    state = runstep(state)
    # print(f"After step {i+1}:")
    # print(DataFrame(state))

print(f"Part 1: number of flashes is : {flashes}")

# Part 2

notall = True
step = 0
state = copy.deepcopy(values)
while notall:
    step += 1
    startflashes = flashes
    state = runstep(state)
    # print(f"step: {step} startflashes: {startflashes} flashes: {flashes} delta: {flashes - startflashes}")
    if flashes == startflashes + 100:
        notall = False
        print(f"Part 2: {step}")
