import copy
import re
from collections import defaultdict


def update_polymer_string(in_str: str, pair_insertion_rules: dict, num_iter: int) -> dict:

    # Save first and last element to adjust later, as we are tracking pairs 
    # and all elements will belong to exactly two pairs, except the first and
    # last element.
    first_el = in_str[0]
    last_el = in_str[-1]
    pair_dict_in = {key: 0 for key in pair_insertion_rules.keys()}

    # Create and count pairs from string
    for index, element in enumerate(in_str[:-1]):
        pair_dict_in[element + in_str[index + 1]] += 1
    
    # Derive pair creation rules from pair insertion rules.
    pair_creation_dict = {key: [key[0] + value, value + key[1]] for key, value in zip(pair_insertion_rules.keys(), pair_insertion_rules.values())}

    # Evolution of pairs over certain number of iterations.
    for i in range(num_iter):
        new_pair_dict = {key: 0 for key in pair_insertion_rules.keys()}
        for key in pair_creation_dict.keys():
            for pair in pair_creation_dict[key]:
                new_pair_dict[pair] += pair_dict_in[key]

        pair_dict_in = new_pair_dict

    # Count the letters from final pairs.
    letter_counts = defaultdict(lambda: 0)
    for key in pair_dict_in.keys():
        for letter in key:
            letter_counts[letter] += pair_dict_in[key]

    # Account for first and last element only belonging to one pair.
    letter_counts[first_el] += 1
    letter_counts[last_el] += 1

    # Divide by 2, as each element belongs to exactly two pairs.
    for key in letter_counts.keys():
        letter_counts[key] /= 2

    return letter_counts


if __name__ == "__main__":

    with open('input', 'r') as f:
        in_lines = f.readlines()

    in_str = in_lines[0][:-1]
    pair_insertion_rules = {}

    for element in in_lines[2:]:
        match = re.findall(r'[A-Z]+', element)
        pair_insertion_rules[match[0]] = match[1]

    letter_counts = update_polymer_string(in_str, pair_insertion_rules, 40)
    print(max(letter_counts.values()) - min(letter_counts.values()))
