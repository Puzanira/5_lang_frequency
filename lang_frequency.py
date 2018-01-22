import sys
from collections import Counter


def form_dictionary(filepath):
    dictionary = []
    with open(filepath, "r") as file:
        for line in file:
            dictionary.extend(line.split())
    return dictionary


def get_most_frequent_words(words):
    words_counter = Counter(words)
    max_words = 10
    word_pairs = \
        [(-pair[1], pair[0]) for pair in words_counter.most_common(max_words)]
    for i in sorted(word_pairs):
        print(i[0] * -1, i[1])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: define file path")
        print("Usage example: python lang_frequency.py <path to file>")
    else:
        words_list = form_dictionary(sys.argv[1])
        get_most_frequent_words(words_list)
