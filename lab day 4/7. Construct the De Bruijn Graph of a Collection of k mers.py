patterns = []
with open('rosalind_ba3e.txt') as file:
    patterns = file.readlines()
    patterns = [pattern.rstrip() for pattern in patterns]

adjList = {}
patternLen = len(patterns[0])
for pattern in patterns:
    currentPattern = pattern[:-1]
    nextPattern = pattern[1:]
    if currentPattern not in adjList.keys():
        adjList[currentPattern] = nextPattern
    else:
        adjList[currentPattern] += f',{nextPattern}'

output = ''
sortedItemList = sorted(adjList.items())
for item in sortedItemList:
    output += f'{item[0]} -> {item[1]}\n'
with open('../lab day 5/output.txt', 'w') as file:
    file.write(output)