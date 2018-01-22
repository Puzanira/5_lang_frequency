import sys
from collections import Counter


def form_dictionary(filepath):
    dictionary = []
    with open(filepath, "r") as my_file:
        for line in my_file:
            dictionary.extend(line.split())
    return dictionary


def get_most_frequent_words(words):
    words_counter = Counter(words)
    max_words = 10
    word_pairs = \
        [(-pair[1], pair[0]) for pair in words_counter.most_common(max_words)]
    for pair in sorted(word_pairs):
        print(pair[0] * -1, pair[1])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: define file path")
        print("Usage example: python lang_frequency.py <path to file>")
    else:
        words_list = form_dictionary(sys.argv[1])
        get_most_frequent_words(words_list)
