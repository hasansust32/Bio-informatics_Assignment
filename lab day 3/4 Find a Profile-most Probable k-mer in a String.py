import re

symbol_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


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


text = ''
k = 0
profile_matrix = []
with open('rosalind_ba2c.txt') as file:
    stuffs = file.readlines()
    char_regex = re.compile('[^a-zA-Z]')
    text = char_regex.sub('', stuffs[0])
    k = int(stuffs[1])
    for row in stuffs[2:]:
        all_floats = re.findall(r"[-+]?\d*\.\d+|\d+", row)
        all_floats = [float(i) for i in all_floats]
        profile_matrix.append(all_floats)

print(get_most_probable_k_mer(profile_matrix, text, k))
