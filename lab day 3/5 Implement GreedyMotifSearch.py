import re
import numpy as np

symbol_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def get_profile_from_motifs(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile = [[0.0]*k, [0.0]*k, [0.0]*k, [0.0]*k]
    for text in motifs:
        for i in range(k):
            index = symbol_index[text[i]]
            profile[index][i] += 1
    np_profile = np.array(profile)/t
    profile = np_profile.tolist()
    return profile


def get_probability(profile, pattern):
    pattern_len = len(pattern)
    probability = 1
    for i in range(pattern_len):
        probability *= profile[symbol_index[pattern[i]]][i]
    return probability


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


def greedy_motif_search(dna, k, t):
    best_motifs = [text[:k] for text in dna]
    best_score = get_score_from_motifs(best_motifs)
    text_len = len(dna[0])
    for i in range(text_len-k+1):
        current_motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            current_profile = get_profile_from_motifs(current_motifs)
            # print(np.array(current_profile))
            most_probable_pattern = get_most_probable_k_mer(current_profile, dna[j], k)
            current_motifs.append(most_probable_pattern)
        # print(current_motifs)
        current_score = get_score_from_motifs(current_motifs)
        if current_score < best_score:
            best_motifs = current_motifs
            best_score = current_score
    return best_motifs




dna = []
k = 0
t = 0
with open('rosalind_ba2d.txt') as file:
    stuffs = file.readlines()
    digits = re.findall(r'\d+', stuffs[0])
    k = int(digits[0])
    t = int(digits[1])
    dna = stuffs[1:]
    char_regex = re.compile('[^a-zA-Z]')
    dna = [char_regex.sub('', line) for line in dna]



best_motifs = greedy_motif_search(dna, k, t)
print('\n'.join(best_motifs))