PUZZLE_INPUT = "hxbxwxba"

alpha = "abcdefghijklmnopqrstuvwxyz"
triples = [alpha[i : i + 3] for i in range(26 - 2)]


def is_valid(password):
    # Rule 1
    r1 = False
    for t in triples:
        if t in password:
            r1 = True
            break
    # Rule 2
    r2 = True
    for c in ["i", "o", "l"]:
        if c in password:
            r2 = False
            break
    # Rule 3
    i = 0
    num_pairs = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            num_pairs += 1
            # Extra step to avoid overlapping pairs like aaa
            i += 1
        i += 1
    r3 = num_pairs > 1
    return r1 and r2 and r3


# assert not is_valid("hijklmmn")
# assert not is_valid("abbceffg")
# assert not is_valid("abbcegjk")
# assert is_valid("abcdffaa")
# assert is_valid("ghjaabcc")

# Convert the password to base 26
as_base_26 = []

for c in PUZZLE_INPUT:
    as_base_26.append(alpha.index(c))
print(as_base_26)


def increment(password):
    carry = 1
    for i in range(len(password)):
        if carry:
            password[~i] += 1
            carry = 0
            if password[~i] > 25:
                carry = 1
                password[~i] = 0
            if password[~i] in [alpha.index("i"), alpha.index("o"), alpha.index("l")]:
                password[~i] += 1
        if carry == 0:
            break
    return password


def as_string(password):
    chars = []
    for c in password:
        chars.append(alpha[c])
    return "".join(chars)


valid = False
while not valid:
    as_base_26 = increment(as_base_26)
    valid = is_valid(as_string(as_base_26))

# hxbxxyzz
print(f"answer = {as_string(as_base_26)}")

# Part 2 - go fro the next valid password
valid = False
while not valid:
    as_base_26 = increment(as_base_26)
    valid = is_valid(as_string(as_base_26))

# hxcaabcc
print(f"answer = {as_string(as_base_26)}")
