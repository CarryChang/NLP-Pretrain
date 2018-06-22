# coding=utf-8
import codecs
#过滤停用词
#########################直接使用原文过滤效果更好
def filter():
    stopwords = []
    delstopwords_alltxt = []
    delstopwords_singletxt = []
    # i = 'key/ltp_cu.txt'
    i = 'key/pure_cut.txt'
    file=codecs.open(i, 'r',encoding='utf-8')
    #####st是停用词表
    st = codecs.open('stopwords/stopwords.txt', 'r',encoding='utf-8')
    #########delstopwords_result是处理后的结果
    delstopwords_result = codecs.open('result/pure_filter.txt','w',encoding='utf-8')
    ############加载停用词
    for line in st:
        line = line.strip()
        stopwords.append(line)
    print (u'正在过滤停用词.')
    ###############
    for singletext_result in file:
        words = singletext_result.strip().split(" ")
        for word in words:
            if word not in stopwords:
                delstopwords_singletxt.append(word+' ')
        delstopwords_singletxt.append('\n')
    delstopwords_alltxt.append(delstopwords_singletxt)
    for delstopwords_singletxt in delstopwords_alltxt:
        for everyword in delstopwords_singletxt:
            delstopwords_result.write(everyword)
        delstopwords_result.write('\n')
    delstopwords_result.close()
    print ('success')
def run():
    filter()
if __name__ == '__main__':
    run()
