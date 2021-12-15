f = open('input.txt', 'r')
values = []
for line in f:
    if line.strip():
        values.append(line.strip())

lens = {0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6}

# Part 1

easycount = 0
for val in values:
    right = val.split('|')[1]
    rvals = right.split()
    rlens = [len(x) for x in rvals]
    reasy = [x for x in rlens if x in [2, 4, 3, 7]]
    easycount += len(reasy)

print(f"Part 1 solution: {easycount}")

# Part 2
print("Part 2:")
valid = {0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"}

def incommon(str1, str2):
    newstr = ''.join(set(str1).intersection(str2))
    return len(newstr)

def fingerprint(ts, str2):
    return (incommon(ts[1], str2), incommon(ts[4], str2), incommon(ts[7], str2))

total = 0
for val in values:
    left = val.split('|')[0].split()
    right = val.split('|')[1].split()
    ts = {}
    ts[1] = [x for x in left if len(x) == 2][0]
    ts[4] = [x for x in left if len(x) == 4][0]
    ts[7] = [x for x in left if len(x) == 3][0]
    ts[8] = [x for x in left if len(x) == 7][0]

    ts[0] = [x for x in left if len(x) == 6 and fingerprint(ts, x) == (2, 3, 3)][0]
    ts[2] = [x for x in left if len(x) == 5 and fingerprint(ts, x) == (1, 2, 2)][0]
    ts[3] = [x for x in left if len(x) == 5 and fingerprint(ts, x) == (2, 3, 3)][0]
    ts[5] = [x for x in left if len(x) == 5 and fingerprint(ts, x) == (1, 3, 2)][0]
    ts[6] = [x for x in left if len(x) == 6 and fingerprint(ts, x) == (1, 3, 2)][0]
    ts[9] = [x for x in left if len(x) == 6 and fingerprint(ts, x) == (2, 4, 3)][0]

    invts = {''.join(sorted(v)): k for k, v in ts.items()}
    print(invts)

    vals = [str(invts[''.join(sorted(x))]) for x in right]
    output = int(''.join(vals))
    print(vals, output)
    total = total + output

print(f"Part 2: {total}")
