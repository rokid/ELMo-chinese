import os
import jieba


import re, collections
def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return pairs
def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

vocab = {'l o w </w>' : 5, 'l o w e r </w>' : 2,
'n e w e s t </w>':6, 'w i d e s t </w>':3}

num_merges = 10
for i in range(num_merges):
    pairs = get_stats(vocab)
    best = max(pairs, key=pairs.get)
    vocab = merge_vocab(best, vocab)
    print(best)


def recursive_cut(line):
    result = []
    for big_word in jieba.lcut(line,HMM=False):
            subword_list = get_subword_list(big_word)
            if isinstance(subword_list, list):
                go_subword_list(subword_list,result)
            elif isinstance(subword_list, str):
                result.append(subword_list)
            else:
                print("error")
    return result

def isEN(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

def isZH(char):
    if not ('\u4e00' <= char <= '\u9fa5'):
        return False
    return True


def get_subword_list(big_word):
    if not isZH(big_word[0]):
        return big_word
    if len(big_word)>3:
        jieba.del_word(big_word)
        return jieba.lcut(big_word, HMM=False)
    else:
        return big_word

def go_subword_list(input_list,result):
    for big_word in input_list:
        if len(big_word)>3:
            subword_list = get_subword_list(big_word)
            if isinstance(subword_list,list):
                go_subword_list(subword_list,result)
            elif isinstance(subword_list,str):
                result.append(subword_list)
            else:
                print("error")
        else:
            result.append(big_word)


def isDigit(x):
    try:
        x=int(x)
        return isinstance(x,int)
    except ValueError:
        return False


vocab = set()
dir = os.listdir("../../data")
for file in dir:
    print(file)
    f = open("../../data/" + file, mode="r", encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        word_list = recursive_cut(line)
        for word in word_list:
            if isEN(word[0]):
                continue
            if isDigit(word[0]):
                continue
            vocab.add(word.replace("\n",""))


f2 = open("../../vocab/cn_vocab2",mode="w",encoding="utf-8")

f2.write("</S>")
f2.write("\n")
f2.write("<S>")
f2.write("\n")
f2.write("<UNK>")
f2.write("\n")

for word in list(vocab):
    if word!="" and word!=" ":
        f2.write(word)
        f2.write("\n")
f2.close()
