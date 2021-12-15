f = open('input.txt', 'r')
values = []
for line in f:
    values.append(int(line))

counter = 0

# Part 1:

for x in range(len(values)-1):
    if values[x+1] > values[x]:
        counter += 1

print(f"part 1: {counter}")


# Part 2:

counter = 0
for x in range(2, len(values)-1):
    lsum = sum([values[i] for i in range(x-2, x+1)])
    rsum = sum([values[j] for j in range(x-1, x+2)])
    # print(f"lsum: {lsum}, rsum: {rsum}")
    if rsum > lsum:
        counter += 1

print(f"part 2: {counter}")
