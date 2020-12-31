PUZZLE_INPUT = "1113222113"

# PUZZLE_INPUT = "111221"


def solve(sequence):
    popped = None
    count = 0
    collector = []

    for i, v in enumerate(sequence):
        if popped:
            if v == popped:
                count += 1
            else:
                collector.append(str(count))
                collector.append(popped)
                popped = v
                count = 1
        else:
            popped = v
            count = 1
    collector.append(str(count))
    collector.append(popped)
    return "".join(collector)


answer = PUZZLE_INPUT
for i in range(40):
    answer = solve(answer)

# 252594
print(f"answer = {len(answer)}")


# Part 2
# Do it another 10 times

for i in range(10):
    answer = solve(answer)

# 3579328
print(f"answer = {len(answer)}")
