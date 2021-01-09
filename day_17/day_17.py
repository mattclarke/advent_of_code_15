with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [int(x) for x in PUZZLE_INPUT.strip().split("\n")]
# print(puzzle_input)

containers = set()

for p in puzzle_input:
    containers.add((p, len(containers)))

TARGET = 150

SOLUTIONS = set()


def solve(containers, used, total):
    for con in containers:
        if total + con[0] == TARGET:
            global SOLUTIONS
            new_used = used[:]
            new_used.append(con)
            SOLUTIONS.add(tuple(sorted(new_used)))
        elif total + con[0] > TARGET:
            # Dead end
            continue
        else:
            new_used = used[:]
            new_used.append(con)
            new_containers = set(containers)
            new_containers.remove(con)
            solve(new_containers, new_used, total + con[0])


solve(containers, [], 0)

# 654
print(f"answer = {len(SOLUTIONS)}")

min_cons = 1000
count = 0

for s in SOLUTIONS:
    if len(s) == min_cons:
        count += 1
    elif len(s) < min_cons:
        min_cons = len(s)
        count = 1

# 57
print(f"answer = {count}")
