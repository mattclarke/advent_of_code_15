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
weight_per_compartment = total_weight // 4
print(weight_per_compartment)
best = None

def find_combos(target, weights, level=0):
    ways_to_make_weight = set()

    def _find_combos(weights, used, total, level):
        global best
        for w in weights:
            if level == 0 and best and len(used) > len(best):
                return

            if total + w == target:
                n_used = used[:]
                n_used.append(w)
                if level == 0:
                    n_weights = weights
                    n_weights.remove(w)
                    try:
                        possible = len(find_combos(target, n_weights, 1)) > 0
                    except:
                        if best and len(n_used) < len(best):
                            best = tuple(n_used)
                        elif best and len(n_used) == len(best):
                            curr_sum = reduce(lambda x, y: x * y, best)
                            new_sum = reduce(lambda x, y: x * y, n_used)
                            if new_sum < curr_sum:
                                best = tuple(n_used)
                        elif not best:
                            best = tuple(n_used)
                        print(best, reduce(lambda x, y: x * y, best))
                elif level == 1:
                    n_weights = weights
                    n_weights.remove(w)
                    ways_to_make_weight.add(tuple(n_used))
                    try:
                        possible = len(find_combos(target, n_weights, 2)) > 0
                    except:
                        raise
                elif level == 2:
                    n_weights = weights
                    n_weights.remove(w)
                    ways_to_make_weight.add(tuple(n_used))
                    try:
                        possible = len(find_combos(target, n_weights, 3)) > 0
                    except:
                        raise
                elif level == 3:
                    n_weights = weights
                    n_weights.remove(w)
                    ways_to_make_weight.add(tuple(n_used))
                    raise KeyError
                continue
            elif total + w > target:
                continue
            # elif used and w < used[~0]:
            #     # No point checking both (1, 2) and (2, 1) for example
            #     continue
            else:
                n_used = used[:]
                n_used.append(w)
                n_weights = weights[:]
                n_weights.remove(w)
                _find_combos(n_weights, n_used, total + w, level)

    _find_combos(weights, [], 0, level)
    if level == 0:
        return best
    return ways_to_make_weight


# Solution is most likely to contain big numbers
puzzle_input.reverse()
possible_combos = find_combos(weight_per_compartment, puzzle_input)
print(best)
best_so_far = None
best_so_far_sum = reduce(lambda x, y: x * y, best)

# 11266889531
print(f"answer = {best_so_far_sum}")

# Part 2
# 77387711

