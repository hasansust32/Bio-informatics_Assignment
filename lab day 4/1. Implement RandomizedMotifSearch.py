import re
import random
import numpy as np

symbol_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def get_most_probable_k_mer(profile, text, k):
    most_probable_k_mer = ''
    max_probability = -1
    text_len = len(text)
    for i in range(text_len - k + 1):
        pattern = text[i:i + k]
        probability = get_probability(profile, pattern)
        if probability > max_probability:
            max_probability = probability
            most_probable_k_mer = pattern
    return most_probable_k_mer


def get_most_probable_k_mers(profile, dna, k):
    k_mers = []
    for text in dna:
        k_mers.append(get_most_probable_k_mer(profile, text, k))
    return k_mers


def get_probability(profile, pattern):
    pattern_len = len(pattern)
    probability = 1
    for i in range(pattern_len):
        probability *= profile[symbol_index[pattern[i]]][i]
    return probability


def get_profile_from_motifs(motifs, pseudo_count=False):
    k = len(motifs[0])
    t = len(motifs)
    count = 0.0
    if pseudo_count:
        count = 1.0
    profile = [[count]*k, [count]*k, [count]*k, [count]*k]
    for text in motifs:
        for i in range(k):
            index = symbol_index[text[i]]
            profile[index][i] += 1
    divisor = t
    if pseudo_count:
        divisor += 4
    np_profile = np.array(profile)/divisor
    profile = np_profile.tolist()
    return profile


def get_score_from_motifs(motifs):
    t = len(motifs)
    motif_len = len(motifs[0])
    score = 0
    for i in range(motif_len):
        count = {}
        best_count = 0
        for motif in motifs:
            symbol = motif[i]
            if symbol not in count.keys():
                count[symbol] = 1
            else:
                count[symbol] += 1
            if count[symbol] > best_count:
                best_count = count[symbol]
        score += (t-best_count)
    return score


def get_random_motifs(dna, k):
    text_len = len(dna[0])
    t = len(dna)
    random_motifs = []
    for i in range(t):
        random_index = random.randint(0, text_len-k)
        pattern = dna[i][random_index: random_index+k]
        random_motifs.append(pattern)
    return random_motifs


def randomized_motif_search(dna, k, t):
    text_len = len(dna[0])
    best_motifs = get_random_motifs(dna, k)
    best_score = get_score_from_motifs(best_motifs)
    current_motifs = best_motifs.copy()
    while True:
        profile = get_profile_from_motifs(current_motifs, True)
        current_motifs = get_most_probable_k_mers(profile, dna, k)
        current_score = get_score_from_motifs(current_motifs)
        # print(current_score)
        if current_score < best_score:
            best_score = current_score
            best_motifs = current_motifs
        else:
            return best_motifs, best_score


dna = []
k = 0
t = 0
with open('rosalind_ba2f.txt') as file:
    stuffs = file.readlines()
    digits = re.findall(r'\d+', stuffs[0])
    k = int(digits[0])
    t = int(digits[1])
    dna = stuffs[1:]
    char_regex = re.compile('[^a-zA-Z]')
    dna = [char_regex.sub('', line) for line in dna]


best_score = k*t
best_motifs = []
for i in range(1000):
    motifs, score = randomized_motif_search(dna, k, t)
    if best_score > score:
        best_motifs = motifs
        best_score = score
    print(i+1)
print('\n'.join(best_motifs), best_score)
