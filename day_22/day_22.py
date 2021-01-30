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
    updated_effects = {}

    # For part 2 - not making any difference!!!!!
    # player["Hit Points"] -= 1
    # if player["Hit Points"] < 1:
    #     return player, boss, active_effects

    for i in range(2):
        # print(player, boss)
        if len(active_effects) > 3:
            assert False

        for n, d in active_effects.items():
            new_d = d - 1
            if new_d > 0:
                updated_effects[n] = new_d
        active_effects = deepcopy(updated_effects)
        updated_effects = {}

        for effect, duration in active_effects.items():
            boss["Hit Points"] -= SPELLS[effect][1]
            if player["Armor"] == 0:
                player["Armor"] = SPELLS[effect][2]
            player["Mana"] += SPELLS[effect][4]

        if i == 0 and player["Hit Points"] > 0:
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

    return player, boss, active_effects


best_mana_cost = 10000000000000


def solve(player, boss, active_effects, mana_cost):
    global best_mana_cost

    for spell in SPELLS.keys():
        if spell in active_effects and active_effects[spell] > 1:
            continue

        n_mana_cost = mana_cost + SPELLS[spell][0]
        if n_mana_cost > best_mana_cost:
            continue

        n_player, n_boss, n_active_effects = fight_two_rounds(
            deepcopy(player), deepcopy(boss), spell, deepcopy(active_effects)
        )
        if n_player["Hit Points"] < 1 or n_player["Mana"] < 1:
            continue
        elif n_boss["Hit Points"] < 1:
            best_mana_cost = min(best_mana_cost, n_mana_cost)
            continue
        solve(n_player, n_boss, n_active_effects, n_mana_cost)


# solve(deepcopy(PLAYER), deepcopy(BOSS), {}, 0)

# Part 1 = 900
print(f"answer = {best_mana_cost}")

active_effects = {}
boss = deepcopy(BOSS)
player = deepcopy(PLAYER)
mana_cost = 0


def do_spell(spell, boss, player, active_effects):
    if spell in ["Magic Missile", "Drain"]:
        boss["Hit Points"] -= SPELLS[spell][1]
        player["Hit Points"] += SPELLS[spell][3]
    else:
        active_effects[spell] = SPELLS[spell][5]
    player["Mana"] -= SPELLS[spell][0]
    return SPELLS[spell][0]


def apply_effects(active_effects, player, boss):
    to_remove = []

    for effect, duration in active_effects.items():
        boss["Hit Points"] -= SPELLS[effect][1]
        if player["Armor"] == 0:
            player["Armor"] = SPELLS[effect][2]
        player["Mana"] += SPELLS[effect][4]
        active_effects[effect] -= 1
        if active_effects[effect] == 0:
            to_remove.append(effect)

    for r in to_remove:
        del active_effects[r]


def do_boss(damage, armor):
    player_loss_b = 0
    if boss["Hit Points"] > 1:
        player_loss_b = damage - armor
        if player_loss_b < 1:
            player_loss_b = 1
    return player_loss_b


BEST = 100000000000


def is_finished(player, boss, mana_cost, spell_list):
    global BEST
    if (
            player["Hit Points"] < 1
            or player["Mana"] < 1
            or boss["Hit Points"] < 1
    ):
        if boss["Hit Points"] < 1:
            print("boss lost", mana_cost, spell_list)
            BEST = min(BEST, mana_cost)
        return True
    return False


for a in SPELLS.keys():
    active_effects_a = deepcopy(active_effects)
    player_a = deepcopy(PLAYER)
    boss_a = deepcopy(BOSS)
    mana_cost_a = mana_cost

    # Apply effects
    apply_effects(active_effects_a, player_a, boss_a)

    # Do spell
    spell_list_a = [a]
    mana_cost_a += do_spell(a, boss_a, player_a, active_effects_a)
    # if mana_cost_a > BEST:
    #     continue

    if is_finished(player_a, boss_a, mana_cost_a, spell_list_a):
        continue

    # Boss turn
    # Apply effects
    apply_effects(active_effects_a, player_a, boss_a)

    player_loss_a = do_boss(boss_a["Damage"], player_a["Armor"])
    player_a["Hit Points"] -= player_loss_a

    if is_finished(player_a, boss_a, mana_cost_a, spell_list_a):
        continue

    for b in SPELLS.keys():
        active_effects_b = deepcopy(active_effects_a)
        player_b = deepcopy(player_a)
        boss_b = deepcopy(boss_a)
        mana_cost_b = mana_cost_a

        # Apply effects
        apply_effects(active_effects_b, player_b, boss_b)

        if b in active_effects_b:
            continue

        # Do spell
        spell_list_b = spell_list_a[:]
        spell_list_b.append(b)
        mana_cost_b += do_spell(b, boss_b, player_b, active_effects_b)
        # if mana_cost_b > BEST:
        #     continue

        if is_finished(player_b, boss_b, mana_cost_b, spell_list_b):
            continue

        # Boss turn
        # Apply effects
        apply_effects(active_effects_b, player_b, boss_b)

        player_loss_b = do_boss(boss_b["Damage"], player_b["Armor"])
        player_b["Hit Points"] -= player_loss_b

        if is_finished(player_b, boss_b, mana_cost_b, spell_list_b):
            continue

        for c in SPELLS.keys():
            active_effects_c = deepcopy(active_effects_b)
            player_c = deepcopy(player_b)
            boss_c = deepcopy(boss_b)
            mana_cost_c = mana_cost_b

            # Apply effects
            apply_effects(active_effects_c, player_c, boss_c)

            if c in active_effects_c:
                continue

            # Do spell
            spell_list_c = spell_list_b[:]
            spell_list_c.append(c)
            mana_cost_c += do_spell(c, boss_c, player_c, active_effects_c)
            # if mana_cost_c > BEST:
            #     continue

            if is_finished(player_c, boss_c, mana_cost_c, spell_list_c):
                continue

            # Boss turn
            # Apply effects
            apply_effects(active_effects_c, player_c, boss_c)

            player_loss_c = do_boss(boss_c["Damage"], player_c["Armor"])
            player_c["Hit Points"] -= player_loss_c

            if is_finished(player_c, boss_c, mana_cost_c, spell_list_c):
                continue

            for d in SPELLS.keys():
                active_effects_d = deepcopy(active_effects_c)
                player_d = deepcopy(player_c)
                boss_d = deepcopy(boss_c)
                mana_cost_d = mana_cost_c

                # Apply effects
                apply_effects(active_effects_d, player_d, boss_d)

                if d in active_effects_d:
                    continue

                # Do spell
                spell_list_d = spell_list_c[:]
                spell_list_d.append(d)
                mana_cost_d += do_spell(d, boss_d, player_d, active_effects_d)
                if mana_cost_d >= BEST:
                    continue

                if is_finished(player_d, boss_d, mana_cost_d, spell_list_d):
                    continue

                # Boss turn
                # Apply effects
                apply_effects(active_effects_d, player_d, boss_d)

                player_loss_d = do_boss(boss_d["Damage"], player_d["Armor"])
                player_d["Hit Points"] -= player_loss_d

                if is_finished(player_d, boss_d, mana_cost_d, spell_list_d):
                    continue

                for e in SPELLS.keys():
                    active_effects_e = deepcopy(active_effects_d)
                    player_e = deepcopy(player_d)
                    boss_e = deepcopy(boss_d)
                    mana_cost_e = mana_cost_d

                    # Apply effects
                    apply_effects(active_effects_e, player_e, boss_e)

                    if e in active_effects_e:
                        continue

                    # Do spell
                    spell_list_e = spell_list_d[:]
                    spell_list_e.append(e)
                    mana_cost_e += do_spell(e, boss_e, player_e, active_effects_e)
                    if mana_cost_e >= BEST:
                        continue

                    if is_finished(player_e, boss_e, mana_cost_e, spell_list_e):
                        continue

                    # Boss turn
                    # Apply effects
                    apply_effects(active_effects_e, player_e, boss_e)

                    player_loss_e = do_boss(boss_e["Damage"], player_e["Armor"])
                    player_e["Hit Points"] -= player_loss_e

                    if is_finished(player_e, boss_e, mana_cost_e, spell_list_e):
                        continue

                    for f in SPELLS.keys():
                        active_effects_f = deepcopy(active_effects_e)
                        player_f = deepcopy(player_e)
                        boss_f = deepcopy(boss_e)
                        mana_cost_f = mana_cost_e

                        # Apply effects
                        apply_effects(active_effects_f, player_f, boss_f)

                        if f in active_effects_f:
                            continue

                        # Do spell
                        spell_list_f = spell_list_e[:]
                        spell_list_f.append(f)
                        mana_cost_f += do_spell(f, boss_f, player_f,
                                                active_effects_f)
                        if mana_cost_f >= BEST:
                            continue

                        if is_finished(player_f, boss_f, mana_cost_f, spell_list_f):
                            continue

                        # Boss turn
                        # Apply effects
                        apply_effects(active_effects_f, player_f, boss_f)

                        player_loss_f = do_boss(boss_f["Damage"],
                                                player_f["Armor"])
                        player_f["Hit Points"] -= player_loss_f

                        if is_finished(player_f, boss_f, mana_cost_f, spell_list_f):
                            continue

                        for g in SPELLS.keys():
                            active_effects_g = deepcopy(active_effects_f)
                            player_g = deepcopy(player_f)
                            boss_g = deepcopy(boss_f)
                            mana_cost_g = mana_cost_f

                            # Apply effects
                            apply_effects(active_effects_g, player_g, boss_g)

                            if g in active_effects_g:
                                continue

                            # Do spell
                            spell_list_g = spell_list_f[:]
                            spell_list_g.append(g)
                            mana_cost_g += do_spell(g, boss_g, player_g,
                                                    active_effects_g)
                            if mana_cost_g >= BEST:
                                continue

                            if is_finished(player_g, boss_g, mana_cost_g, spell_list_g):
                                continue

                            # Boss turn
                            # Apply effects
                            apply_effects(active_effects_g, player_g, boss_g)

                            player_loss_g = do_boss(boss_g["Damage"],
                                                    player_g["Armor"])
                            player_g["Hit Points"] -= player_loss_g

                            if is_finished(player_g, boss_g, mana_cost_g, spell_list_g):
                                continue

                            for h in SPELLS.keys():
                                active_effects_h = deepcopy(active_effects_g)
                                player_h = deepcopy(player_g)
                                boss_h = deepcopy(boss_g)
                                mana_cost_h = mana_cost_g

                                # Apply effects
                                apply_effects(active_effects_h, player_h,
                                              boss_h)

                                if h in active_effects_h:
                                    continue

                                # Do spell
                                spell_list_h = spell_list_g[:]
                                spell_list_h.append(h)
                                mana_cost_h += do_spell(h, boss_h, player_h,
                                                        active_effects_h)
                                if mana_cost_h >= BEST:
                                    continue

                                if is_finished(player_h, boss_h, mana_cost_h, spell_list_h):
                                    continue

                                # Boss turn
                                # Apply effects
                                apply_effects(active_effects_h, player_h,
                                              boss_h)

                                player_loss_h = do_boss(boss_h["Damage"],
                                                        player_h["Armor"])
                                player_h["Hit Points"] -= player_loss_h

                                if is_finished(player_h, boss_h, mana_cost_h, spell_list_h):
                                    continue

                                for i in SPELLS.keys():
                                    active_effects_i = deepcopy(
                                        active_effects_h)
                                    player_i = deepcopy(player_h)
                                    boss_i = deepcopy(boss_h)
                                    mana_cost_i = mana_cost_h

                                    # Apply effects
                                    apply_effects(active_effects_i, player_i,
                                                  boss_i)

                                    if i in active_effects_i:
                                        continue

                                    # Do spell
                                    spell_list_i = spell_list_h[:]
                                    spell_list_i.append(i)
                                    mana_cost_i += do_spell(i, boss_i, player_i,
                                                            active_effects_i)
                                    if mana_cost_i >= BEST:
                                        continue

                                    if is_finished(player_i, boss_i,
                                                   mana_cost_i, spell_list_i):
                                        continue

                                    # Boss turn
                                    # Apply effects
                                    apply_effects(active_effects_i, player_i,
                                                  boss_i)

                                    player_loss_i = do_boss(boss_i["Damage"],
                                                            player_i["Armor"])
                                    player_i["Hit Points"] -= player_loss_i

                                    if is_finished(player_i, boss_i,
                                                   mana_cost_i, spell_list_i):
                                        continue

                                    for j in SPELLS.keys():
                                        active_effects_j = deepcopy(
                                            active_effects_i)
                                        player_j = deepcopy(player_i)
                                        boss_j = deepcopy(boss_i)
                                        mana_cost_j = mana_cost_i

                                        # Apply effects
                                        apply_effects(active_effects_j,
                                                      player_j, boss_j)

                                        if j in active_effects_j:
                                            continue

                                        # Do spell
                                        spell_list_j = spell_list_i[:]
                                        spell_list_j.append(j)
                                        mana_cost_j += do_spell(j, boss_j,
                                                                player_j,
                                                                active_effects_j)
                                        if mana_cost_j >= BEST:
                                            continue

                                        if is_finished(player_j, boss_j,
                                                       mana_cost_j, spell_list_j):
                                            continue

                                        # Boss turn
                                        # Apply effects
                                        apply_effects(active_effects_j,
                                                      player_j, boss_j)

                                        player_loss_j = do_boss(
                                            boss_j["Damage"],
                                            player_j["Armor"])
                                        player_j["Hit Points"] -= player_loss_j

                                        if is_finished(player_j, boss_j,
                                                       mana_cost_j, spell_list_j):
                                            continue

                                        for k in SPELLS.keys():
                                            active_effects_k = deepcopy(
                                                active_effects_j)
                                            player_k = deepcopy(player_j)
                                            boss_k = deepcopy(boss_j)
                                            mana_cost_k = mana_cost_j

                                            # Apply effects
                                            apply_effects(active_effects_k,
                                                          player_k, boss_k)

                                            if k in active_effects_k:
                                                continue

                                            # Do spell
                                            spell_list_k = spell_list_j[:]
                                            spell_list_k.append(k)
                                            mana_cost_k += do_spell(k, boss_k,
                                                                    player_k,
                                                                    active_effects_k)
                                            if mana_cost_k >= BEST:
                                                continue

                                            if is_finished(player_k, boss_k,
                                                           mana_cost_k, spell_list_k):
                                                continue

                                            # Boss turn
                                            # Apply effects
                                            apply_effects(active_effects_k,
                                                          player_k, boss_k)

                                            player_loss_k = do_boss(
                                                boss_k["Damage"],
                                                player_k["Armor"])
                                            player_k[
                                                "Hit Points"] -= player_loss_k

                                            if is_finished(player_k, boss_k,
                                                           mana_cost_k, spell_list_k):
                                                continue
print(BEST)
