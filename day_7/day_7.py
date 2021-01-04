with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)


def solve(commands):
    wires = {}

    while commands:
        line = commands.pop(0)

        try:
            parts = [x.strip() for x in line.split("->")]

            if "AND" in parts[0]:
                temp = parts[0].split(" AND ")
                a = int(temp[0]) if temp[0][0].isdigit() else wires[temp[0]]
                b = int(temp[1]) if temp[1][0].isdigit() else wires[temp[1]]
                wires[parts[1]] = a & b
            elif "OR" in parts[0]:
                temp = parts[0].split(" OR ")
                a = int(temp[0]) if temp[0][0].isdigit() else wires[temp[0]]
                b = int(temp[1]) if temp[1][0].isdigit() else wires[temp[1]]
                wires[parts[1]] = a | b
            elif "LSHIFT" in parts[0]:
                temp = parts[0].split(" LSHIFT ")
                a = int(temp[0]) if temp[0][0].isdigit() else wires[temp[0]]
                b = int(temp[1]) if temp[1][0].isdigit() else wires[temp[1]]
                wires[parts[1]] = a << b
            elif "RSHIFT" in parts[0]:
                temp = parts[0].split(" RSHIFT ")
                a = int(temp[0]) if temp[0][0].isdigit() else wires[temp[0]]
                b = int(temp[1]) if temp[1][0].isdigit() else wires[temp[1]]
                wires[parts[1]] = a >> b
            elif "NOT" in parts[0]:
                w = parts[0].replace("NOT ", "")
                w = int(w) if w[0].isdigit() else wires[w]
                wires[parts[1]] = ~w
                if wires[parts[1]] <= 0:
                    wires[parts[1]] += 65536
            else:
                # Assignment
                wires[parts[1]] = (
                    int(parts[0]) if parts[0][0].isdigit() else wires[parts[0]]
                )
        except Exception as err:
            # Cannot do instruction yet, so re-add
            commands.append(line)
    return wires


commands = puzzle_input[:]
wires = solve(commands)

# 956
print(f"answer = {wires['a']}")

# Part 2
# Replace the assignment to "b" with the value for "a" from part 1
commands = puzzle_input[:]

for i in range(len(commands)):
    if commands[i].endswith(" -> b"):
        commands[i] = f"{wires['a']} -> b"
        break

wires = solve(commands)

# 40149
print(f"answer = {wires['a']}")

