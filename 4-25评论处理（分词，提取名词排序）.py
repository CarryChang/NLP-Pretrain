# -*- coding: utf-8 -*-
from pyltp import Segmentor
from pyltp import Postagger
def run():
    ####直接对预料进行处理
    segmentor = Segmentor()  # 初始化实例
    # segmentor.load('cws.model')  # 加载模型,不加载字典
    segmentor.load_with_lexicon('cws.model', 'userdict.txt') # 加载模型,加载用户字典
    postagger = Postagger() # 初始化实例
    postagger.load('pos.model')  # 加载模型
    # sentence1=['操作简单','洗衣效果好']
    # sentence1=open('key/pinglun_filter_all1.txt','r',encoding='utf-8')
    sentence1=open('key/pinglun_resource.txt','r',encoding='utf-8')
    pinglun_n=open('key1/pinglun_n_all.txt','w',encoding='utf-8')
    pinglun_n_cut=open('key1/pinglun_n_cut.txt','w',encoding='utf-8')
    pinglun_n_tag=open('key1/pinglun_n_tag.txt','w',encoding='utf-8')
    for sentence in sentence1:
        words = segmentor.segment(sentence)  # 分词
        #默认可以这样输出
        # print ('\t'.join(words))
        pinglun_n_cut.write('\t'.join(words)+'\n')
        postags = postagger.postag(words)  # 词性标注
        for word,tag in zip(words,postags):
            #############选择词性输出
            # print (word+'/'+tag)
            pinglun_n_tag.write(word+'/'+tag+'\n')
            ############只选出名词，字数大于1
            if tag == 'n'and len(word)>1:
                # print (word+'/'+tag)
                ##########只输出我们想要的词，去除词性
                pinglun_n.write(word+'\n')
    segmentor.release()  # 释放模型
    postagger.release()
    sentence1.close()
    pinglun_n.close()
    pinglun_n_cut.close()
    pinglun_n_tag.close()
    #######################开始统计词频加上制作词典
    word_df = []
    in_file = 'key1/pinglun_n_all.txt'
    out_file = 'key1/pinglun_n_dict.txt'
    word_count = {}#统计词频的字典
    for line in open(in_file,'r',encoding='utf-8'):
        words = line.strip().split("\n")
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    out = open(out_file,'w',encoding='utf-8')
    for word in word_count.keys():
        if word is not '':
            #按词频的顺序遍历字典的每个元素
            out.write(word)
            word_df.append([word, str(word_count.get(word))])
            out.write('\n')
    print ('制作的字典已经保存到key1/pinglun_n_dict.txt')
    out.close()
    # number = 0
    with open("key1/pinglun_n_reverse.txt", 'w',encoding='utf-8') as wf2:
        word_df.sort(key=lambda x: int(x[1]),reverse=True)
        wf2.truncate()
        for item in word_df:
            for word in item:
                wf2.write(word + '\t')
            wf2.write('\n')
            # number += 1
            # if number == 50:
            #     break
        print('字典倒序排序已经保存到key1/pinglun_n_reverse.txt ')
    wf2.close()
def pic():
    flieName = 'key1/pinglun_n_reverse.txt'
    inFile = open(flieName, 'r',encoding='utf-8')#以只读方式打开某fileName文件
    #定义两个空list，用来存放文件中的数据
    X = []
    y = []
    for line in inFile:
        trainingSet = line.split('\t') #对于每一行，按','把数据分开，这里是分成两部分
        X.append(trainingSet[0]) #第一部分，即文件中的第一列数据逐一添加到list X 中
        y.append(trainingSet[1]) #第二部分，即文件中的第二列数据逐一添加到list y 中
    y =[int(y) for y in y if y]
    print(X, y)
    fig = plt.figure('形容词词频图')
    plt.bar(range(len(y)), y,color='green',tick_label=X)
    plt.xlabel("words")
    plt.ylabel("numbers")
    plt.title("n of numbers")
    plt.show()
    plt.close()
if __name__ == '__main__':
    import time
    from pylab import *
    import matplotlib.pyplot as plt
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    ########开始分词+标记词性+按词性输出
    starttime1=time.clock()
    run()
    # pic()
    endtime1=time.clock()
    print('开始分词+标记词性+按词性输出+画图所用时间为(单位s)：')
    T1=endtime1-starttime1
    print (T1)
