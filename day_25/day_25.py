target_row = 2978 - 1  # Adjust to zero index
target_column = 3083 - 1

num_rows = target_row + target_column + 1

previous_code = 20151125

row = 1
column = 0
finished = False

while row < num_rows and not finished:
    for i, j in zip(reversed(range(row + 1)), range(row + 1)):
        previous_code = (previous_code * 252533) % 33554393
        if i == target_row and j == target_column:
            finished = True
            break
    row += 1

# 2650453
print(f"answer = {previous_code}")
