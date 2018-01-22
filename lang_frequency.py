import sys
from collections import Counter
import re


def load_data(filepath):
    file = open(filepath, 'r')
    try:
        text = file.read()
    finally:
        file.close()
    all_words_list = re.findall(r"[\w']+", text)
    return all_words_list


def get_most_frequent_words(words):
    words_counter = Counter(words)
    max_words = 10
    common_words = words_counter.most_common(max_words)
    word_pairs = [(pair[1], pair[0]) for pair in common_words]
    return word_pairs


def print_words_list(word_dict):
    for count, word in word_dict:
        print(count, word)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: define file path")
        print("Usage example: python lang_frequency.py <path to file>")
    else:
        words_list = load_data(sys.argv[1])
        sorted_list = get_most_frequent_words(words_list)
        print_words_list(sorted_list)
