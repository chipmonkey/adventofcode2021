def calculate_score(plist, tgt):
    score = 0
    for pos in plist:
        score += abs(tgt - pos)
    return score


def calculate_score2(plist, tgt):
    score = 0
    for pos in plist:
        dist = abs(tgt - pos)
        if dist > 0: 
            score += (dist * (dist + 1)) / 2
    return score

f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

values = values[0].split(',')
print(values)
values = list(map(int, values))
print(values)

# Part 1

maxv = max(values)
print(maxv)

score = [calculate_score(values, x) for x in range(1, maxv+1)]

best = min(score)
besti = score.index(best)

print(f"best = {best} at position {besti}")

# Part 2

score = [calculate_score2(values, x) for x in range(1, maxv+1)]
print(score)

best = min(score)
besti = score.index(best)

print(f"best = {best} at position {besti}")
