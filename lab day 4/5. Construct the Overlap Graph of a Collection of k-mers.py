import re

patterns = []
with open('rosalind_ba3c.txt') as file:
    patterns = file.readlines()
    char_regex = re.compile('[^a-zA-Z]')
    patterns = sorted([char_regex.sub('', pattern) for pattern in patterns])

adjList = []
for i in range(len(patterns)):
    firstPattern = patterns[i]
    for j in range(len(patterns)):
        if i == j:
            continue
        secondPattern = patterns[j]
        if firstPattern[1:] == secondPattern[:-1]:
            adjList.append(f'{firstPattern} -> {secondPattern}')

# print(adjList)

with open('../lab day 5/output.txt', 'w') as file:
    file.write('\n'.join(adjList))