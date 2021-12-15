from bingo import bingo

f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

numbers = values[0].split(',')
boards = values[1:]

boards = [list(line.split()) for line in boards if line != '']


# Part 1
game = bingo(numbers, boards)
game.find_winner()

score = game.final_score

print(f"part 1: game: {score}")


# Part 2
game.find_last_winner()
score = game.loser_score

print(f"part2: game: {score}")
