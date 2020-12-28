PUZZLE_INPUT = b"yzbqklnj"

# PUZZLE_INPUT = b"pqrstuv"

# Simple way is to use Python's hashlib
import hashlib

nonce = 1

while True:
    m = hashlib.md5(PUZZLE_INPUT + str(nonce).encode())
    # print(m.hexdigest())
    if m.hexdigest().startswith("00000"):
        break
    nonce += 1

# 282749
print(f"answer = {nonce}")

# Part 2
nonce = 1

while True:
    m = hashlib.md5(PUZZLE_INPUT + str(nonce).encode())
    # print(m.hexdigest())
    if m.hexdigest().startswith("000000"):
        break
    nonce += 1

# 9962624
print(f"answer = {nonce}")
