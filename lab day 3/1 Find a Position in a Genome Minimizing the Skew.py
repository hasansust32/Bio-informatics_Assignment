import numpy as np

dna = ''
with open('rosalind_ba1f.txt') as file:
    dna = file.read().replace('\n', '')

skew_map = {'C': -1, 'G': 1, 'T': 0, 'A': 0}
skew = np.empty(len(dna), dtype=np.int16)
count = 0
for i, char in enumerate(dna):
    count += skew_map[char]
    skew[i] = count

min = min(skew)
indices = np.where(skew == min)[0] + 1
print(indices)
