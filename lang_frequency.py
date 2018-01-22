import sys
from collections import Counter


def load_data(filepath):
    words = []
    with open(filepath, "r") as file:
        for line in file:
            words.extend(line.split())
    return words


def get_most_frequent_words(words):
    counter = Counter(words)
    pairs = [(-pair[1], pair[0]) for pair in counter.most_common(10)]
    for i in sorted(pairs):
        print(i[0] * -1, i[1])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: define file path")
        print("Usage example: python lang_frequency.py <path to file>")
    else:
        words = load_data(sys.argv[1])
        get_most_frequent_words(words)
