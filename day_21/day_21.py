BOSS = {
    "Hit Points": 104,
    "Damage": 8,
    "Armor": 1,
}

PLAYER = {
    "Hit Points": 100,
    "Damage": 0,
    "Armor": 0,
}


def fight(player, boss):
    turn = 0

    while player["Hit Points"] > 0 and boss["Hit Points"] > 0:
        if turn % 2 == 0:
            damage = player["Damage"] - boss["Armor"]
            if damage < 1:
                damage = 1
            boss["Hit Points"] -= damage
        else:
            damage = boss["Damage"] - player["Armor"]
            if damage < 1:
                damage = 1
            player["Hit Points"] -= damage
        turn += 1
    return player["Hit Points"] > 0


WEAPONS = {
    "Dagger": (8, 4, 0,),
    "Shortsword": (10, 5, 0,),
    "Warhammer": (25, 6, 0,),
    "Longsword": (40, 7, 0,),
    "Greataxe": (74, 8, 0,),
}

ARMOR = {
    "Leather": (13, 0, 1),
    "Chainmail": (31, 0, 2),
    "Splintmail": (53, 0, 3),
    "Bandedmail": (75, 0, 4),
    "Platemail": (102, 0, 5),
}

RINGS = {
    "Damage +1": (25, 1, 0),
    "Damage +2": (50, 2, 0),
    "Damage +3": (100, 3, 0),
    "Defense +1": (20, 0, 1),
    "Defense +2": (40, 0, 2),
    "Defense +3": (80, 0, 3),
}

armor = list(ARMOR.keys())
armor.insert(0, None)
rings = list(RINGS.keys())
rings.insert(0, None)
rings.insert(0, None)

cheapest_win = 1000000000000
expensive_lose = 0

for w in WEAPONS.values():
    cost = w[0]
    PLAYER["Damage"] = w[1]

    for a in armor:
        if a:
            cost += ARMOR[a][0]
            PLAYER["Armor"] += ARMOR[a][2]
        for r1 in rings:
            if r1:
                ring1 = RINGS[r1]
                cost += ring1[0]
                PLAYER["Damage"] += ring1[1]
                PLAYER["Armor"] += ring1[2]
            for r2 in rings:
                if r2 and r2 != r1:
                    ring2 = RINGS[r2]
                    cost += ring2[0]
                    PLAYER["Damage"] += ring2[1]
                    PLAYER["Armor"] += ring2[2]
                if fight(dict(PLAYER), dict(BOSS)):
                    cheapest_win = min(cheapest_win, cost)
                else:
                    expensive_lose =max(expensive_lose, cost)
                if r2 and r2 != r1:
                    ring2 = RINGS[r2]
                    cost -= ring2[0]
                    PLAYER["Damage"] -= ring2[1]
                    PLAYER["Armor"] -= ring2[2]
            if r1:
                ring1 = RINGS[r1]
                cost -= ring1[0]
                PLAYER["Damage"] -= ring1[1]
                PLAYER["Armor"] -= ring1[2]
        if a:
            cost -= ARMOR[a][0]
            PLAYER["Armor"] -= ARMOR[a][2]

# 78
print(f"answer = {cheapest_win}")

# 148
print(f"answer = {expensive_lose}")



