import itertools
from math import prod

f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

zerocounts = {'{': 0, '[': 0, '(': 0, '<': 0}
opens = '{[(<'
closes = '}])>'
score = [1197, 57, 3, 25137]

def syntaxscore(row):
    counts = zerocounts
    stack = []
    for x in row:
        if x in closes:
            place = closes.index(x)
            if opens[place] == stack[-1]:
                stack.pop()
                # print(f"stack: {stack}")
            else:
                # print(f"expected {opens[place]}, got {x}")
                return score[place]
        else:
            stack.append(x)
            # print(f"stack: {stack}")
    return 0    

                
def syntaxcomplete(row):
    counts = zerocounts
    stack = []
    for x in row:
        if x in closes:
            place = closes.index(x)
            if opens[place] == stack[-1]:
                stack.pop()
                # print(f"stack: {stack}")
            else:
                # print(f"expected {opens[place]}, got {x}")
                return score[place]
        else:
            stack.append(x)
            # print(f"stack: {stack}")

    return stack

def stackscore(stack):
    shortscores = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for x in reversed(stack):
        score *= 5
        score += shortscores[x]

    return score
        
    
# Part 1 and 2

total = 0
for row in values:
    total += syntaxscore(row)

print(f"part 1: {total}")


# Part 2:
scores = []
for row in values:
    if syntaxscore(row) == 0:
        stack = syntaxcomplete(row)
        scores.append(stackscore(stack))

scores.sort()
index = len(scores) // 2
print(f"part 2: middle score is: {scores[index]}")
