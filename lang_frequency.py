import sys
import re
from collections import Counter
import os


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        read_data = file_handler.read()
    return read_data


def get_most_frequent_words(text):
    words_list = re.findall(r"[\w']+", text)
    words_counter = Counter(words_list)
    max_words = 10
    return words_counter.most_common(max_words)


def print_words_list(word_dict):
    for word, count in word_dict:
        print(count, word)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Error: define file path')
        print('Usage example: python lang_frequency.py <path to file>')
    else:
        if os.path.isfile(sys.argv[1]):
            text = load_data(sys.argv[1])
            ten_most_common_words = get_most_frequent_words(text)
            print_words_list(ten_most_common_words)
        else:
            print('Error: No such file in directory')
