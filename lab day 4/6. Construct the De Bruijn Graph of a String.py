Text = ''
k = 0
with open('rosalind_ba3d.txt') as file:
    k = int(file.readline().strip())
    Text = file.readline().strip()

adjList = {}
for i in range(len(Text) - k + 1):
    pattern = Text[i: i + k - 1]
    nextPattern = Text[i + 1: i + k]
    if pattern not in adjList.keys():
        adjList[pattern] = [nextPattern]
    else:
        adjList[pattern].append(nextPattern)


output = ''
sortedItemList = sorted(adjList.items())
for item in sortedItemList:
    value = ','.join(item[1])
    output += f'{item[0]} -> {value}\n'
# output = output[:-1]
with open('../lab day 5/output.txt', 'w') as file:
    file.write(output)