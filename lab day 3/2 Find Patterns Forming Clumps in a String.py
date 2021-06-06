from Bio.Seq import Seq
import re


def get_pattern_count(text, pattern):
    seq = Seq(text)
    return seq.count_overlap(pattern)

genome = ''
k = 0
l = 0
t = 0
with open('rosalind_ba1e.txt') as file:
    stuffs = file.readlines()
    char_regex = re.compile('[^a-zA-Z]')
    int_regex = re.compile('[^0-9]')
    genome = char_regex.sub('', stuffs[0])
    numbers = stuffs[1].split(' ')
    k = int(int_regex.sub('', numbers[0]))
    l = int(int_regex.sub('', numbers[1]))
    t = int(int_regex.sub('', numbers[2]))

genome_len = len(genome)
clump = []

for i in range(genome_len - l + 1):
    current_genome = genome[i:i+l]
    current_genome_len = len(current_genome)
    for j in range(current_genome_len - k + 1):
        pattern = current_genome[j:j+k]
        pattern_count = get_pattern_count(current_genome, pattern)
        if pattern_count >= t and pattern not in clump:
            clump.append(pattern)
print(' '.join(clump))
