from functools import reduce

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 1
# 2
# 3
# 4
# 5
# 7
# 8
# 9
# 10
# 11
# """

puzzle_input = [int(x) for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

total_weight = reduce(lambda x, y: x + y, puzzle_input)


def check_next_compartment(target, weights, level=0, part2=False):
    def _find_combos(weights, used, total, level):
        for w in weights:
            if total + w == target:
                n_used = used[:]
                n_used.append(w)
                if level == 1:
                    n_weights = weights
                    n_weights.remove(w)

                    if part2:
                        ans = check_next_compartment(target, n_weights, 2, part2)
                        if ans:
                            return True
                    else:
                        if check_remainder(target, n_weights):
                            return True
                elif level == 2:
                    # For Part 2 only
                    n_weights = weights
                    n_weights.remove(w)
                    if check_remainder(target, n_weights):
                        return True
                continue
            elif total + w > target:
                continue
            elif used and w > used[~0]:
                # No point checking both (1, 2) and (2, 1) for example
                continue
            else:
                n_used = used[:]
                n_used.append(w)
                n_weights = weights[:]
                n_weights.remove(w)
                if _find_combos(n_weights, n_used, total + w, level):
                    return True
        return False

    return _find_combos(weights, [], 0, level)


def check_remainder(target, weights):
    # As long as there are some weights left over then it is fine
    # as they must add up to the target.
    if not weights:
        return False

    return True


def find_optimum_first_compartment(target, weights, part2=False):
    best_combo = [None]

    def _find_combos(weights, used, total):
        for w in weights:
            if total + w == target:
                n_used = used[:]
                n_used.append(w)
                n_weights = weights
                n_weights.remove(w)

                is_valid = check_next_compartment(target, n_weights, 1, part2)

                if is_valid:
                    if not best_combo[0]:
                        best_combo[0] = n_used
                    else:
                        if len(n_used) < len(best_combo[0]):
                            best_combo[0] = n_used
                        elif reduce(lambda x, y: x * y, n_used) < reduce(
                            lambda x, y: x * y, best_combo[0]
                        ):
                            best_combo[0] = n_used
                continue
            elif total + w > target:
                continue
            elif used and w > used[~0]:
                # No point checking both (1, 2) and (2, 1) for example
                continue
            else:
                n_used = used[:]
                n_used.append(w)

                # Cannot beat the best so give up
                if best_combo[0] and len(n_used) > len(best_combo[0]):
                    continue

                n_weights = weights[:]
                n_weights.remove(w)
                _find_combos(n_weights, n_used, total + w)

    for w in weights:
        n_weights = weights[:]
        n_weights.remove(w)
        _find_combos(n_weights, [w], w)
    return best_combo[0]


# Solution is most likely to contain big numbers, so start from the big end.
puzzle_input.reverse()

weight_per_compartment = total_weight // 3
best_combo = find_optimum_first_compartment(weight_per_compartment, list(puzzle_input))

# 11266889531 (113, 109, 107, 103, 83, 1)
print(f"answer = {reduce(lambda x, y: x * y, best_combo)}")

# Part 2
weight_per_compartment = total_weight // 4
best_combo = find_optimum_first_compartment(weight_per_compartment, puzzle_input, True)

# 77387711 (113, 109, 103, 61, 1)
print(f"answer = {reduce(lambda x, y: x * y, best_combo)}")
