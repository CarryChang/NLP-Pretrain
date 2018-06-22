# coding=utf-8
import multiprocessing
from gensim import corpora, models, similarities
#要点：直接导入其中的名词进去
def run():
    #分词+选词
    cont = open('result/pure_n.txt','r',encoding='utf-8')
    nwordall = []
    for words in cont:
        real_word = words.strip().split(" ")
        nwordall.append(real_word)
    print('马上开始w2v')
    model = models.Word2Vec(nwordall, window=5, size=100,min_count=10, workers=multiprocessing.cpu_count())
    model.save("model/word2vec_gensim")
    model.wv.save_word2vec_format("data/model/word2vec_org",
                                  "data/model/vocabulary",
                                  binary=False)
    print('#############################################')

    sim = model.most_similar(positive=[u'房间'])
    for s in sim:
        print ("word:%s,similar:%s " %(s[0],s[1]))
if __name__ == '__main__':
    import time
    starttime1=time.clock()
    run()
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)