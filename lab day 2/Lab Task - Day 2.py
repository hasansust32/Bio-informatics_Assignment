#!/usr/bin/env python
# coding: utf-8

# # Subtask 1: Reverse Complement

# In[2]:


from Bio.Seq import Seq

def get_reverse_complement(dna):
    seq = Seq(dna)
    reverse_complement = seq.reverse_complement()
    return str(reverse_complement)

dna = 'AAAACCCGGT'
output = get_reverse_complement(dna)
output


# # Subtask 2: Hamming Distance

# In[3]:


def get_hamming_distance(dna1, dna2):
    len_1 = len(dna1)
    len_2 = len(dna2)
    min_len = min(len_1, len_2)
    max_len = max(len_1, len_2)
    hamming_distance = max_len - min_len

    for i in range(min_len):
        if dna1[i] != dna2[i]:
            hamming_distance += 1

    return hamming_distance


dna1 = 'GGGCCGTTGGT'
dna2 = 'GGACCGTTGAC'
distance = get_hamming_distance(dna1, dna2)
distance


# # Subtask 3: Approximate Pattern Matching Problem

# In[4]:


def get_position_of_patterns(text, pattern, d, reverse_complement=False):
    position_list = []
    len_pattern = len(pattern)
    len_text = len(text)
    for i in range(len_text - len_pattern + 1):
        temp_pattern = text[i:i+len_pattern]
        distance = get_hamming_distance(temp_pattern, pattern)
        if distance <= d:
            position_list.append(i)
        if reverse_complement:
            distance = get_hamming_distance(temp_pattern, get_reverse_complement(pattern))
            if distance <= d:
                position_list.append(i)
    return position_list

pattern = 'ATTCTGGA'
text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
d = 3
list_of_positions = get_position_of_patterns(text, pattern, d)
list_of_positions


# # Subtask 4: Frequent Words with Mismatches

# In[5]:


import itertools

def freq_words_with_mismatch(text, k, d, reverse_complement=False):
    symbols = ['A', 'T', 'G', 'C']
    all_possible_patterns = list(itertools.product(symbols, repeat=k))
    freq = 0
    most_frequent_words = []
    for pattern in all_possible_patterns:
        pattern = ''.join(pattern)
        pattern_position_list = get_position_of_patterns(text, pattern, d, reverse_complement)
        pattern_count = len(pattern_position_list)
        if pattern_count > freq:
            most_frequent_words.clear()
            freq = pattern_count
            most_frequent_words.append(pattern)
        elif pattern_count == freq:
            most_frequent_words.append(pattern)
    return most_frequent_words


text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
words = freq_words_with_mismatch(text, k, d)
words


# # Subtask 5: Frequent Words with Mismatches and Reverse Complements

# In[6]:



text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'

k = 4
d = 1
words = freq_words_with_mismatch(text, k, d, True)
words


# # Subtask 6: Implement PatternToNumber

# In[7]:


import itertools

def pattern_to_number(pattern):
    pattern_len = len(pattern)
    symbols = ['A', 'C', 'G', 'T']
    all_patterns = list(itertools.product(symbols, repeat=pattern_len))
    return all_patterns.index(tuple(pattern))

dna = 'AGT'
number = pattern_to_number(dna)
number


# # Subtask 7: Implement NumberToPattern

# In[17]:


import itertools

def number_to_pattern(index, k):
    symbols = ['A', 'C', 'G', 'T']
    all_patterns = list(itertools.product(symbols, repeat=k))
    return ''.join(all_patterns[index])

index = 45
k = 4
dna = number_to_pattern(index, k)
dna

