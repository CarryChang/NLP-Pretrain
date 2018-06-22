# coding=utf-8
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
from snownlp import sentiment
from snownlp.sentiment import Sentiment
def snowanalysis(key_word):
    print(key_word)
    print('正在执行...')
    ##############看清楚对于‘r’的使用
    key_txt_neg = open('keywords/emotion/%s_neg.txt'%key_word,'r',encoding='utf-8')
    key_txt_pos = open('keywords/emotion/%s_pos.txt'%key_word,'r',encoding='utf-8')
    key_score = open('keywords/score/%s_total_score.txt'%key_word,'w',encoding='utf-8')
    score_pos = 0
    score_neg = 0
    for score in key_txt_pos:
        if score.startswith('0' or '1'):
            score_pos += float(score)
    key_score.write(key_word+'积极情绪总分')
    key_score.write(str(score_pos))
    key_score.write('\n')
    for score in key_txt_neg:
        if score.startswith('0' or '1'):
            ###########增加消极情绪极性
            stand_score = 1 - float(score)
            score_neg += stand_score
    key_score.write(key_word+'消极情绪总分')
    key_score.write(str(score_neg))
    print('success')
    key_score.close()
    #################
if __name__ == '__main__':
    key_words = {'环境','娱乐','位置','价格','特色','设施','餐饮','交通','卫生','服务','体验'}
    for key_word in key_words:
        snowanalysis(key_word)
