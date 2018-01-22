import sys

def load_data(filepath):
    words = dict()
    with open(filepath, "r") as file:
        for line in file:
            lst = [word for word in line.split()]
            for word in lst:
                word = word.lower()
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
    return words


def get_most_frequent_words(words):
    count = 0
    for i in sorted(words.items(), key=lambda x:(-x[1],x[0])):
        if (count < 10):
            print(count + 1, i[0], ':= ', i[1])
            count += 1
        else:
            break

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Error: define file path")
        print ("Usage example: python lang_frequency.py <path to file>")
    else:
         words = load_data(sys.argv[1])
         get_most_frequent_words(words)
