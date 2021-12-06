from lanternfish import fish

f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

print(values)
values = values[0].split(',')
print(values)
values = list(map(int, values))
print(values)

# Part 1 and 2
f = fish(values)

score = f.thing2()

print(f"part 1: game: {score}")

