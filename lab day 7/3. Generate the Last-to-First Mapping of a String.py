with open('rosalind_ba9k.txt') as file:
    last_col = file.readline().rstrip()
    index = int(file.readline().rstrip())

target_symbol = last_col[index]
symbol_number = 1
first_col = sorted(last_col)
for i in range(index):
    if last_col[i] == target_symbol:
        symbol_number += 1

symbol_count = 0
for i, symbol in enumerate(first_col):
    if symbol == target_symbol:
        symbol_count += 1
        if symbol_count == symbol_number:
            output = str(i)
            break 
print(output)
with open('output.txt', 'w') as file:
    file.write(output)