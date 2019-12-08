# coding: utf-8
import collections

INPUT = '../data/neko.num'
SIZE = 13938
TENUM = 28
SINUM = 24


def load_data():
    with open(INPUT, 'r') as f:
        lines = f.readlines()

    return lines


def get_bi_word(lines):

    words = []
    f = False
    for line in lines:
        text = line.replace('\n', '').split()
        for word in text:
            if f:
                words.append(word)
                f = False
            if int(word) == TENUM:
                f = True

    return words


def count_bi_word(lines):
    words = get_bi_word(lines)
    c = collections.Counter(words)

    count_bi = [0 for i in range(SIZE)]
    for i, co in c.items():
        count_bi[int(i)] = co/len(words)
    return count_bi


if __name__ == '__main__':
    lines = load_data()
    count = count_bi_word(lines)
    with open('../model/bigram.model', 'w') as f:
        for c in count:
            f.write(str(c)+'\n')
