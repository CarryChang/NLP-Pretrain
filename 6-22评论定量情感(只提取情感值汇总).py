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
    # key_txt_neg = open('keywords/emotion_1/%s_neg.txt'%key_word,'w',encoding='utf-8')
    # key_txt_pos = open('keywords/emotion_1/%s_pos.txt'%key_word,'w',encoding='utf-8')
    score_pos = 0
    score_neg = 0
    for li in key_txt:
        s = SnowNLP(li)
        score = s.sentiments
        score_pos = []
        score_neg = []
        # sentiments_list.append(score)
        ##############使用3-7分更准确
        if score > 0.7000:
            print(score)
            score_pos += float(score)
            # key_txt_pos.write(li)
        elif score < 0.3000:
            print(score)
            # score_neg += float(score)
            # key_txt_neg.write(li)
    #################
    print('指标积极总分')
    print(score_pos)
    # print('指标消极总分')
    # print(score_neg)
    # plt.hist(sentiments_list, bins=np.arange(0, 1, 0.01))
    # plt.xlabel("情感值")
    # plt.ylabel("评论数目")
    # plt.title(key_word+'-情感极性分布图')
    # plt.show()
if __name__ == '__main__':
    # key_words = {'环境','娱乐','位置','价格','特色','设施','餐饮','交通','卫生','服务','体验'}
    key_words = {'娱乐','特色'}
    for key_word in key_words:
        snowanalysis(key_word)
