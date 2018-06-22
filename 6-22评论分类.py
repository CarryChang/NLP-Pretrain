# coding=utf-8
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
from snownlp import sentiment
from snownlp.sentiment import Sentiment
def snowanalysis(key_word):
    print(key_word)
    sentiments_list = []
    print('正在执行...')
    key_txt = open('keywords/key_list/%s.txt'%key_word,'r',encoding='utf-8')
    key_txt_neg = open('keywords/emotion/%s_neg.txt'%key_word,'w',encoding='utf-8')
    key_txt_pos = open('keywords/emotion/%s_pos.txt'%key_word,'w',encoding='utf-8')
    for li in key_txt:
        s = SnowNLP(li)
        score = s.sentiments
        sentiments_list.append(score)
        if s.sentiments > 0.7000:
            key_txt_pos.write(li+str(score)+'\n')
        elif s.sentiments < 0.3000:
            key_txt_neg.write(li+str(score)+'\n')
if __name__ == '__main__':
    key_words = {'环境','娱乐','位置','价格','特色','设施','餐饮','交通','卫生','服务','体验'}
    for key_word in key_words:
        snowanalysis(key_word)