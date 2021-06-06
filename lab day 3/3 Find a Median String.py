import re
import itertools


def get_hamming_distance(dna1, dna2):
    dna_len = len(dna1)
    hamming_distance = 0

    for i in range(dna_len):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance


def get_text_distance(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    min_distance = pattern_len

    for i in range(text_len-pattern_len+1):
        temp_pattern = text[i:i+pattern_len]
        distance = get_hamming_distance(temp_pattern, pattern)
        if min_distance > get_hamming_distance(temp_pattern, pattern):
            min_distance = distance
    return min_distance


def get_dna_distance(dna, pattern):
    pattern_len = len(pattern)
    distance = 0
    for text in dna:
        text_distance = get_text_distance(text, pattern)
        distance += text_distance
    return distance


dna = []
k = 0
with open('rosalind_ba2b.txt') as file:
    stuffs = file.readlines()
    char_regex = re.compile('[^a-zA-Z]')
    int_regex = re.compile('[^0-9]')
    k = int(int_regex.sub('', stuffs[0]))
    dna = stuffs[1:]
    dna = [char_regex.sub('', text) for text in dna]

symbols = 'GACT'
all_patterns = list(itertools.product(symbols, repeat=k))
min_distance = k*len(dna)
median = ''
for pattern in all_patterns:
    pattern = ''.join(pattern)
    distance = get_dna_distance(dna, pattern)
    if min_distance > distance:
        min_distance = distance
        median = pattern
print(median)

