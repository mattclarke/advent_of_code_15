from copy import deepcopy

BOSS = {
    "Hit Points": 51,
    "Damage": 9,
    "Armor": 0,
}

PLAYER = {
    "Hit Points": 50,
    "Damage": 0,
    "Armor": 0,
    "Mana": 500,
}


SPELLS = {
    # Cost, damage, armor, heal, mana, duration
    "Magic Missile": (53, 4, 0, 0, 0, 0),
    "Drain": (73, 2, 0, 2, 0, 0),
    "Shield": (113, 0, 7, 0, 0, 6),
    "Poison": (173, 3, 0, 0, 0, 6),
    "Recharge": (229, 0, 0, 0, 101, 5),
}


# BOSS = {
#     "Hit Points": 14,
#     "Damage": 8,
#     "Armor": 0,
# }
#
# PLAYER = {
#     "Hit Points": 10,
#     "Damage": 0,
#     "Armor": 0,
#     "Mana": 250,
# }


def fight_two_rounds(player, boss, spell, active_effects):
    for i in range(2):
        # Not having this line introduces a subtle bug for part 2
        # where the armor stays are 7 even after the spell has worn off
        player["Armor"] = 0

        for effect, duration in active_effects.items():
            boss["Hit Points"] -= SPELLS[effect][1]
            player["Armor"] += SPELLS[effect][2]
            player["Mana"] += SPELLS[effect][4]

        updated_effects = {}
        for n, d in active_effects.items():
            new_d = d - 1
            if new_d > 0:
                updated_effects[n] = new_d
        active_effects = deepcopy(updated_effects)

        if i == 0:
            # print(f"player casts {spell}")
            if spell in ["Magic Missile", "Drain"]:
                boss["Hit Points"] -= SPELLS[spell][1]
                player["Hit Points"] += SPELLS[spell][3]
            else:
                active_effects[spell] = SPELLS[spell][5]
            player["Mana"] -= SPELLS[spell][0]
        elif player["Hit Points"] > 0:
            if boss["Hit Points"] > 0:
                damage = boss["Damage"] - player["Armor"]
                if damage < 1:
                    damage = 1
                player["Hit Points"] -= damage

        if player["Hit Points"] < 1 or player["Mana"] < 1 or boss["Hit Points"] < 1:
            break

    return player, boss, active_effects


best_mana_cost = 10000000000000


def solve(player, boss, active_effects, mana_cost, part_2=False):
    global best_mana_cost

    for spell in SPELLS.keys():
        if spell in active_effects and active_effects[spell] > 1:
            continue

        n_mana_cost = mana_cost + SPELLS[spell][0]
        if n_mana_cost > best_mana_cost:
            continue

        n_player = deepcopy(player)

        if part_2:
            n_player["Hit Points"] -= 1
            if n_player["Hit Points"] < 1:
                continue

        n_player, n_boss, n_active_effects = fight_two_rounds(
            deepcopy(n_player), deepcopy(boss), spell, deepcopy(active_effects)
        )
        if n_player["Hit Points"] < 1 or n_player["Mana"] < 1:
            continue
        elif n_boss["Hit Points"] < 1:
            best_mana_cost = min(best_mana_cost, n_mana_cost)
            continue
        solve(n_player, n_boss, n_active_effects, n_mana_cost, part_2)


solve(deepcopy(PLAYER), deepcopy(BOSS), {}, 0)

# 900
print(f"answer = {best_mana_cost}")

# Part 2
best_mana_cost = 10000000000000
solve(deepcopy(PLAYER), deepcopy(BOSS), {}, 0, True)

# 1216
print(f"answer = {best_mana_cost}")
