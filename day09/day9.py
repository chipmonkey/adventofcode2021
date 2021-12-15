import itertools
from math import prod

f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

maxx = len(values)

values = [[i for i in x] for x in values]
values = [list(map(int, x)) for x in values]

maxy = len(values[0])


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def islowest(values, x, y, offset, maxx, maxy):
    testx = x + offset[0]
    testy = y + offset[1]
    if testx < 0 or testy < 0 or testx >= maxx or testy >= maxy:
        return True

    if values[x][y] < values[x+offset[0]][y+offset[1]]:
        return True

    return False


def getbasinsize(values, x, y, maxx, maxy):
    result = [(x, y)]  # for the current point
    for offset in dirs:
        testx = x + offset[0]
        testy = y + offset[1]
        if testx < 0 or testy < 0 or testx >= maxx or testy >= maxy:
            continue

        if values[testx][testy] > values[x][y] and values[testx][testy] < 9:
            newvalue = getbasinsize(values, testx, testy, maxx, maxy)
            result.extend(newvalue)

    return result
        

# Part 1 and 2

lowpoints = []
basins = []

for x in range(maxx):
    for y in range(maxy):
        islow = True
        for offset in dirs:
            if not islowest(values, x, y, offset, maxx, maxy):
                islow = False
        if islow:
            lowpoints.append(values[x][y])
            basins.append(getbasinsize(values, x, y, maxx, maxy))

print(f"lowpoints: {lowpoints}")

sizes = [len(set(x)) for x in basins]
sizes.sort()
print(f"Basin sizes: {sizes}")

part1 = sum([1+x for x in lowpoints])
part2 = prod(sizes[-3:])

print(f"Part 1 solution: {part1}")
print(f"Part 2 solution: {part2}")

