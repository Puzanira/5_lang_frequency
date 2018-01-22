import sys
from collections import Counter


def load_data(filepath):
    dictionary = []
    with open(filepath, "r") as file:
        for line in file:
            dictionary.extend(line.split())
    return dictionary


def get_most_frequent_words(words):
    words_counter = Counter(words)
    MAX_WORDS = 10
    word_pairs = \
        [(-pair[1], pair[0]) for pair in words_counter.most_common(MAX_WORDS)]
    for i in sorted(word_pairs):
        print(i[0] * -1, i[1])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: define file path")
        print("Usage example: python lang_frequency.py <path to file>")
    else:
        words_list = load_data(sys.argv[1])
        get_most_frequent_words(words_list)
