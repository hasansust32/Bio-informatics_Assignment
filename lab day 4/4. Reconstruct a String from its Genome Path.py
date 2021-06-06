import re

patterns = []
with open('rosalind_ba3b.txt') as file:
    patterns = file.readlines()
    char_regex = re.compile('[^a-zA-Z]')
    patterns = [char_regex.sub('', pattern) for pattern in patterns]

genome = patterns[0][0:-1]
for pattern in patterns:
    genome += pattern[-1]
print(genome)