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


def get_uni_word(lines):

    words = []
    for line in lines:
        for w in line.replace('\n', '').split():
            words.append(w)

    return words


def count_bi_word(lines):
    words = get_bi_word(lines)
    c = collections.Counter(words)

    count_count = {}
    for i, co in c.items():
        if co in count_count.keys():
            count_count[co] += 1
        else:
            count_count[co] = 1

    # 最尤推定
    freq = sorted(count_count.keys())
    print(freq)

    count_bi = [0 for i in range(SIZE)]
    # count_bi = [count_count[1]/(SIZE-len(words))/len(words)
    #            for i in range(SIZE)]
    for i, co in c.items():
        if freq.index(co) != len(freq)-1:
            after = freq[freq.index(co)+1]
        else:
            after = co
        count_bi[int(i)-1] = (after)*count_count[after] / \
            count_count[co]/len(words)

    # katz
    uni_word_no_bi = [int(g)
                      for g in get_uni_word(lines) if not str(g) in words]
    print(len(set(words)))
    print(len(set(uni_word_no_bi)))

    total = sum(count_bi)
#    zero_c = [1 for i in count_bi if i == 0]
    for w in set(uni_word_no_bi):
        print(w)
        count_bi[w-1] = (1-total)*uni_word_no_bi.count(w)/len(uni_word_no_bi)

    return count_bi


if __name__ == '__main__':
    lines = load_data()
    count = count_bi_word(lines)
    with open('../model/bigram.model', 'w') as f:
        for c in count:
            f.write(str(c)+'\n')
