# coding=UTF-8
#全部切成三字及以下
import jieba

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

#print(recursive_cut("一二三四五六七八九十"))
#print(recursive_cut("十九八七六五四三二一"))