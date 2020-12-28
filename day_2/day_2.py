with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


puzzle_input = PUZZLE_INPUT.strip().split("\n")
print(puzzle_input)

total = 0

for present in puzzle_input:
    l, w, h = (int(x) for x in present.split("x"))
    lw = l * w
    wh = w * h
    hl = h * l
    slack = min(lw, wh, hl)

    total += 2 * lw + 2 * wh + 2 * hl + slack

# 1598415
print(f"answer = {total}")


# Part 2
total = 0

for present in puzzle_input:
    dims = [int(x) for x in present.split("x")]
    dims.sort()
    perimeter = 2 * (dims[0] + dims[1])
    bow = dims[0] * dims[1] * dims[2]
    total += perimeter + bow

# 3812909
print(f"answer = {total}")
