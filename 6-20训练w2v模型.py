# coding=utf-8
import multiprocessing
from gensim import corpora, models, similarities
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
    print('马上开始w2v')
    #参数说明https://blog.csdn.net/fly_time2012/article/details/77444945
    #size为维数为200，窗口长度为10， 最小出现次数为10
    model = models.Word2Vec(nwordall, window=4, sg=1,size=100,min_count=10,alpha=0.025,seed=1,
                            sample=0.001,workers=multiprocessing.cpu_count())
    model.save("model/word2vec_gensim")
    model.wv.save_word2vec_format("model/word2vec_org",
                                  "model/vocabulary",
                                  binary=False)
    print('model saved')
    # sim = model.most_similar(['交通'],topn=10)
    # for s in sim:
    #     print ("word:%s,similar:%s " %(s[0],s[1]))
if __name__ == '__main__':
    import time
    starttime1=time.clock()
    run()
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)