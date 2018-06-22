# coding=utf-8
from gensim import corpora, models, similarities
import numpy as np
#要点：直接导入其中的名词进去
def run():
    #分词+选词
    cont = open('result/pure_n.txt','r',encoding='utf-8')
    nwordall = []
    for words in cont:
        ###########消除空格
        if words.strip() != '':
            real_word = words.strip().split(" ")
            nwordall.append(real_word)
        else:continue
   # 3. 选择后的词生成字典
    dictionary = corpora.Dictionary(nwordall)
    # 生成语料库
    corpus = [dictionary.doc2bow(text) for text in nwordall]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    #########开始训练模型
    print('LDA Model training:')
    # 设置主题的数目
    lda = models.LdaModel(corpus_tfidf,id2word=dictionary,num_topics=100)
    #存储model
    lda.save("model/lda_gensim")
    print('model saved')

if __name__ == '__main__':
    import time
    starttime1=time.clock()
    run()
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)