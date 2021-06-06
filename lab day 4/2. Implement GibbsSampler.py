import re
import random
import numpy as np

symbol_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def get_random_motifs(dna, k):
    text_len = len(dna[0])
    t = len(dna)
    random_motifs = []
    for i in range(t):
        random_index = random.randint(0, text_len-k)
        pattern = dna[i][random_index: random_index+k]
        random_motifs.append(pattern)
    return random_motifs


def get_probability(profile, pattern):
    pattern_len = len(pattern)
    probability = 1
    for i in range(pattern_len):
        probability *= profile[symbol_index[pattern[i]]][i]
    return probability


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


def get_random_pattern_from_text(profile, text, k):
    text_len = len(text)
    sum_score = 0
    motif_score = []
    for i in range(text_len - k + 1):
        pattern = text[i:i + k]
        score = get_probability(profile, pattern)
        sum_score += score
        motif_score.append((pattern, sum_score))

    rand_num = random.random() * sum_score
    for item in motif_score:
        motif = item[0]
        value = item[1]
        if rand_num <= value:
            return motif


def gibbs_sampler(dna, k, t, n):
    current_motifs = get_random_motifs(dna, k)
    best_motifs = current_motifs.copy()
    best_score = get_score_from_motifs(best_motifs)
    for count in range(n):
        ignore_index = random.randint(0, t - 1)
        current_motifs.remove(current_motifs[ignore_index])
        profile = get_profile_from_motifs(current_motifs, True)
        random_motif = get_random_pattern_from_text(profile, dna[ignore_index], k)
        # random_motif = get_most_probable_k_mer(profile, dna[ignore_index], k)
        current_motifs.insert(ignore_index, random_motif)
        current_score = get_score_from_motifs(current_motifs)
        if current_score < best_score:
            best_motifs = current_motifs
            best_score = current_score
        # print(count+1)
    return best_motifs, best_score


dna = []
k = 0
t = 0
n = 0
with open('rosalind_ba2g.txt') as file:
    stuffs = file.readlines()
    digits = re.findall(r'\d+', stuffs[0])
    k = int(digits[0])
    t = int(digits[1])
    n = int(digits[2])
    dna = stuffs[1:]
    char_regex = re.compile('[^a-zA-Z]')
    dna = [char_regex.sub('', line) for line in dna]

best_motifs = []
best_score = 10000000000
for i in range(50):
    motifs, score = gibbs_sampler(dna, k, t, n)
    if score < best_score:
        best_motifs = motifs
        best_score = score
    print(i+1, score)
print('\n'.join(best_motifs), best_score)
