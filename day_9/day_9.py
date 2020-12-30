with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

NODES = {}

for line in puzzle_input:
    line = line.replace(" to ", " ").replace(" = ", " ")
    city1, city2, distance = line.split(" ")

    node = NODES.get(city1, {})
    node[city2] = int(distance)
    NODES[city1] = node

    node = NODES.get(city2, {})
    node[city1] = int(distance)
    NODES[city2] = node
# print(NODES)


distances = []


def solve(current, cities, total_dist):
    if not cities:
        distances.append(total_dist)
        return
    for city in cities:
        solve(city, cities.difference({city}), total_dist + NODES[current][city])
        pass


starting_cities = set(NODES.keys())

for start in starting_cities:
    cities = starting_cities.difference({start})
    solve(start, cities, 0)

# 117
print(f"answer = {min(distances)}")

# Part 2
# 909
print(f"answer = {max(distances)}")
