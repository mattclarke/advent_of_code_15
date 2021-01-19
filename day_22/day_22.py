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
    updated_effects = {}

    # For part 2 - not working!
    # player["Hit Points"] -= 1
    # if player["Hit Points"] < 1:
    #     return player, boss, active_effects

    for i in range(2):
        # print(player, boss)
        for effect, duration in active_effects.items():
            boss["Hit Points"] -= SPELLS[effect][1]
            if player["Armor"] == 0:
                player["Armor"] += SPELLS[effect][2]
            player["Mana"] += SPELLS[effect][4]

        if i == 0:
            # print(f"player casts {spell}")
            if spell in ["Magic Missile", "Drain"]:
                boss["Hit Points"] -= SPELLS[spell][1]
                player["Hit Points"] += SPELLS[spell][3]
            else:
                updated_effects[spell] = SPELLS[spell][5]
            player["Mana"] -= SPELLS[spell][0]
        else:
            if boss["Hit Points"] > 0:
                damage = boss["Damage"] - player["Armor"]
                if damage < 1:
                    damage = 1
                player["Hit Points"] -= damage

        if player["Hit Points"] < 1 or player["Mana"] < 1 or boss["Hit Points"] < 1:
            break

        for n, d in active_effects.items():
            new_d = d - 1
            if new_d > 0:
                updated_effects[n] = new_d
        active_effects = dict(updated_effects)
        updated_effects = {}

    return player, boss, active_effects


best_mana_cost = 10000000000000


def solve(player, boss, active_effects, mana_cost):
    global best_mana_cost

    for spell in SPELLS.keys():
        if spell in active_effects:
            continue

        n_mana_cost = mana_cost + SPELLS[spell][0]
        if n_mana_cost > best_mana_cost:
            continue

        n_player, n_boss, n_active_effects = fight_two_rounds(
            dict(player), dict(boss), spell, dict(active_effects)
        )
        if n_player["Hit Points"] < 1 or n_player["Mana"] < 1:
            continue
        elif n_boss["Hit Points"] < 1:
            best_mana_cost = min(best_mana_cost, n_mana_cost)
            continue
        solve(n_player, n_boss, n_active_effects, n_mana_cost)


solve(dict(PLAYER), dict(BOSS), {}, 0)

# 900
print(f"answer = {best_mana_cost}")
