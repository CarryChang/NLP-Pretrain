# coding=utf-8
from pyltp import Segmentor
from pyltp import Postagger
from gensim import corpora, models, similarities
def run():
    #分词+选词
    cont = open('key/pinglun_resource.txt','r',encoding='utf-8')
    segmentor = Segmentor()  # 初始化实例
    # segmentor.load('cws.model')  # 加载模型,不加载字典
    segmentor.load_with_lexicon('cws.model', 'userdict.txt') # 加载模型,加载用户字典
    postagger = Postagger() # 初始化实例
    postagger.load('pos.model')  # 加载模型
    nwordall = []
    for sentence in cont:
        nword = ['']
        words = segmentor.segment(sentence)  # 分词
        #默认可以这样输出
        # print (' '.join(words))
        postags = postagger.postag(words)  # 词性标注
        for word,tag in zip(words,postags):
            #############选择词性输出
            # print (word+'/'+tag)
            ############只选出副词
            # if tag == 'd':
            #######过滤单个字
            # if((tag == 'n'or tag == 'd' or tag == 'a') and len(word)>1):
            ############使用word2vec相似度计算找取跟名词相近的形容词
            # if((tag == 'a' or tag == 'n') and len(word)>1):
            if((tag == 'n') and len(word)>1):
                # print(word+tag)
                nword.append(word)
        nwordall.append(nword)
    #size为词向量维度数也即是特征值,windows窗口范围,min_count频数小于5的词忽略,workers是线程数，维度高会造成问题
    model = models.word2vec.Word2Vec(nwordall, window=2, min_count=10, workers=100)
    print('#############################################')
    sim = model.most_similar(positive=[u'环境'])
    for s in sim:
        print ("word:%s,similar:%s " %(s[0],s[1]))
if __name__ == '__main__':
    import time
    starttime1=time.clock()
    run()
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)
