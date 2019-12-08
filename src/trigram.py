# coding: utf-8
import collections
from bigram import load_data
from bigram import get_bi_word_
from bigram import get_uni_word


INPUT = '../data/neko.num'
SIZE = 13938
TENUM = 28
SINUM = 24


def get_tr_word_(lines):
    '''
    全体を1文とする
    '''

    words = []
    f = 0
    for word in lines:
        word = int(word)
        if f == 2:
            words.append(word)
        if word == SINUM:
            f = 1
        elif f == 1 and word == TENUM:
            f = 2
        else:
            f = 0

    return words


def count_tr_word(lines):
    '''
    Absolute + Katsの計算
    '''

    tr_words = get_tr_word_(lines)
    c = collections.Counter(tr_words)

    count_count = {}
    for i, co in c.items():
        if co in count_count.keys():
            count_count[co] += 1
        else:
            count_count[co] = 1

    count_bi = [0 for i in range(SIZE)]
    for i, co in c.items():
        count_bi[int(i)-1] = (co-0.5)/len(tr_words)

    # bigram
    bi_word_no_tr = [int(g)
                     for g in get_bi_word_(lines) if not int(g) in tr_words]

    total = sum(count_bi)
    for w in set(bi_word_no_tr):
        count_bi[w-1] = (1-total)*(bi_word_no_tr.count(w) -
                                   0.5)/len(bi_word_no_tr)

    # unigram
    uni_word_no_tr = [int(g)
                      for g in get_uni_word(lines) if int(g) not in tr_words]
    uni_word_no_bi = [int(g)
                      for g in uni_word_no_tr if g not in bi_word_no_tr]
    total = sum(count_bi)
    for w in set(uni_word_no_bi):
        count_bi[w-1] = (1-total)*uni_word_no_bi.count(w)/len(uni_word_no_bi)
    total = sum(count_bi)
    return count_bi


if __name__ == '__main__':
    lines = load_data()
    count = count_tr_word(lines)
    with open('../model/trigram.model', 'w') as f:
        for c in count:
            f.write('{:.17g}'.format(c) + '\n')
