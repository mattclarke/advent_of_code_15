import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

reindeer = {}
reindeer_state = {}

for line in puzzle_input:
    m = re.match(r"^(\w+)\D+(\d+)\D+(\d+)\D+(\d+)", line)
    name, top_speed, ts_time, rest = m.groups()
    reindeer[name] = (int(top_speed), int(ts_time), int(rest))
    reindeer_state[name] = ["RUNNING", int(ts_time), 0]

for _ in range(2503):
    for n, v in reindeer.items():
        if reindeer_state[n][0] == "RUNNING":
            # Add the distance
            reindeer_state[n][2] += v[0]
            # Subtract a second
            reindeer_state[n][1] -= 1
            if reindeer_state[n][1] == 0:
                # Switch to resting
                reindeer_state[n][0] = "RESTING"
                reindeer_state[n][1] = v[2]
        else:
            # Subtract a second
            reindeer_state[n][1] -= 1
            if reindeer_state[n][1] == 0:
                # Switch to running
                reindeer_state[n][0] = "RUNNING"
                reindeer_state[n][1] = v[1]

max_dist = 0
for v in reindeer_state.values():
    max_dist = max(max_dist, v[2])

# 2640
print(f"answer = {max_dist}")

# Part 2
reindeer = {}
reindeer_state = {}
scores = {}

for line in puzzle_input:
    m = re.match(r"^(\w+)\D+(\d+)\D+(\d+)\D+(\d+)", line)
    name, top_speed, ts_time, rest = m.groups()
    reindeer[name] = (int(top_speed), int(ts_time), int(rest))
    reindeer_state[name] = ["RUNNING", int(ts_time), 0]
    scores[name] = 0

for _ in range(2503):
    furthest = []
    furthest_dist = 0

    for n, v in reindeer.items():
        if reindeer_state[n][0] == "RUNNING":
            # Add the distance
            reindeer_state[n][2] += v[0]
            # Subtract a second
            reindeer_state[n][1] -= 1
            if reindeer_state[n][1] == 0:
                # Switch to resting
                reindeer_state[n][0] = "RESTING"
                reindeer_state[n][1] = v[2]
        else:
            # Subtract a second
            reindeer_state[n][1] -= 1
            if reindeer_state[n][1] == 0:
                # Switch to running
                reindeer_state[n][0] = "RUNNING"
                reindeer_state[n][1] = v[1]
        if reindeer_state[n][2] > furthest_dist:
            furthest_dist = reindeer_state[n][2]
            furthest = [n]
        elif reindeer_state[n][2] == furthest_dist:
            furthest.append(n)
    for n in furthest:
        scores[n] += 1

max_dist = 0
for s in scores.values():
    max_dist = max(max_dist, s)

# 1102
print(f"answer = {max_dist}")
