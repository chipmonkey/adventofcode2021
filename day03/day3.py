from submarine import submarine

f = open('input.txt', 'r')
values = []
for line in f:
    values.append(line.strip())

values = [list(value) for value in values]


# Part 1
sub = submarine()
sub.set_report(values)

gamma = sub._gamma_rate(sub.report)
epsilon = sub._epsilon_rate(sub.report)

print(f"part 1: gamma: {gamma} epsilon: {epsilon} solution: {gamma * epsilon}")


# Part 2
oxygen = sub.oxygen_rating()
carbon = sub.carbon_rating()
print(f"oxygen: {oxygen}")
print(f"carbon: {carbon}")
print(f"part 2: sultion: {oxygen * carbon}")
