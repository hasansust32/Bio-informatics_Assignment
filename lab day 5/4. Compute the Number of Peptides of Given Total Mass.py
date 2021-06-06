amino_acid_weight = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                     'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

parentMass = 0
with open('rosalind_ba4d.txt') as file:
    parentMass = int(file.readline().rstrip())

weights = list(set(amino_acid_weight.values()))
ways = [-1] * (parentMass + 1)


def get_ways(mass):
    if mass < 0:
        return 0

    if mass == 0:
        return 1

    if ways[mass] != -1:
        return ways[mass]

    current_ways = 0
    for weight in weights:
        current_ways += get_ways(mass - weight)
    ways[mass] = current_ways
    return current_ways


output = get_ways(parentMass)
print(output)
with open('output.txt', 'w') as file:
    file.write(str(output))
