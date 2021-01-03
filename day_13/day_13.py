import json
import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

relationships = {}

for line in puzzle_input:
    line = (
        line.replace(" happiness units by sitting next to ", " ")
        .replace(" would gain ", " ")
        .replace(" would lose ", " -")
        .replace(".", "")
    )
    name, units, neighbour = line.split(" ")
    relations = relationships.get(name, {})
    relations[neighbour] = int(units)
    relationships[name] = relations
print(relationships)

best_total = -100000


def solve(current, possible_neighbours, total, first):
    global best_total
    if possible_neighbours:
        for name in possible_neighbours:
            new_total = total
            if current:
                # Part 1
                new_total += relationships[current][name] + relationships[name][current]
            solve(name, possible_neighbours.difference({name}), new_total, first)
    else:
        # Done
        if first:
            # Part 1
            total += relationships[current][first] + relationships[first][current]
        if total > best_total:
            best_total = total


neighbours = set(relationships.keys())

# Doesn't matter who we start with as it is a round table
name = "Alice"
solve(name, neighbours.difference({name}), 0, name)

# 733
print(f"answer = {best_total}")

# Part 2
best_total = -100000
name = None  # Represents me
solve(name, neighbours.difference({name}), 0, name)

# 725
print(f"answer = {best_total}")
