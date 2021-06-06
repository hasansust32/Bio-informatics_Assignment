import numpy as np
from Bio.Seq import Seq
import string


def get_pattern_count(text, pattern):
    seq = Seq(text)
    return seq.count_overlap(pattern)


def get_pattern_count_dict(text, length=3):
    pattern_dict = {}
    seq = Seq(text)
    for i in range(len(text) - length + 1):
        pattern = text[i:i + length]
        if pattern in pattern_dict:
            continue
        count = seq.count_overlap(pattern)
        pattern_dict[pattern] = count
    return pattern_dict


def get_most_freq_pattern(text, length=3):
    dict = get_pattern_count_dict(text, length)
    return max(dict, key=dict.get)


def matrix_mul(a, b):
    print(type(a))
    result = []
    try:
        result = np.dot(a, b)
    finally:
        return result


def generate_all_possible_patterns():
    alphabets = string.ascii_uppercase
    patterns = []
    for i in alphabets:
        for j in alphabets:
            for k in alphabets:
                patterns.append(i+j+k)
    return patterns


if __name__ == '__main__':
    text = 'AATATATACGGATCGAA'
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    Y = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]

    print(get_pattern_count(text, 'ATA'))
    print(get_most_freq_pattern(text, 3))
    print(get_pattern_count_dict(text, 3))
    print(matrix_mul(X, Y))
    print(generate_all_possible_patterns())