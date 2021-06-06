with open('rosalind_ba9j.txt') as file:
    last_col = file.readline().rstrip()

first_col = sorted(last_col)
last_col = list(last_col)
symbol_count = {}
new_first_col = []
new_last_col = []
for symbol in first_col:
    if symbol not in symbol_count:
        counter = 1
    else:
        counter = symbol_count[symbol] + 1
    symbol_count[symbol] = counter
    new_first_col.append(f'{symbol}{counter}')


symbol_count = {}
for symbol in last_col:
    if symbol not in symbol_count:
        counter = 1
    else:
        counter = symbol_count[symbol] + 1
    symbol_count[symbol] = counter
    new_last_col.append(f'{symbol}{counter}')

prev_map = {}
for i in range(len(last_col)):
    prev_map[new_first_col[i]] = new_last_col[i]

current_char = prev_map['$1']
text = []
while current_char != '$1':
    text.append(current_char[0])
    current_char = prev_map[current_char]
text.insert(0, '$')
text.reverse()
output = ''.join(text)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)