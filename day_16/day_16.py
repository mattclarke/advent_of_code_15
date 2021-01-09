with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

SUES = {}

for line in puzzle_input:
    name = line[: line.index(":")]
    line = line[line.index(":") + 2 :]
    line = line.replace(",", "")
    parts = line.split(" ")
    info = {}
    i = 0
    while i < len(parts):
        info[parts[i]] = int(parts[i + 1])
        i += 2
    SUES[name] = info

clues = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

CLUES = {}

for clue in clues.strip().split("\n"):
    name, value = clue.split(" ")
    CLUES[name] = int(value)

possible_sues = set(SUES.keys())

for n, v in CLUES.items():
    for sue, info in SUES.items():
        if sue not in possible_sues:
            continue
        for ni, vi in info.items():
            if n == ni:
                if v != vi:
                    possible_sues.remove(sue)

# 213
print(f"answer = {possible_sues}")


# Part 2
def comparator(name, reading, value):
    if name in ["cats:", "trees:"]:
        return value > reading
    elif name in ["pomeranians:", "goldfish:"]:
        return value < reading
    else:
        return reading == value


possible_sues = set(SUES.keys())

for n, v in CLUES.items():
    for sue, info in SUES.items():
        if sue not in possible_sues:
            continue
        for ni, vi in info.items():
            if n == ni:
                if not comparator(n, v, vi):
                    possible_sues.remove(sue)

# 323
print(f"answer = {possible_sues}")
