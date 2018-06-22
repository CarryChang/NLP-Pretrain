# coding=utf-8
import codecs
#过滤停用词
#########################直接使用原文过滤效果更好
def filter():
    stopwords = []
    delstopwords_alltxt = []
    delstopwords_singletxt = []
    i = input('输入需要处理的文件的（txt）的路径（格式为key/pinglun.txt）：')
    file=codecs.open(i, 'r',encoding='utf-8')
    #####st是停用词表
    st = codecs.open('stopwords/stopwords.txt', 'r',encoding='utf-8')
    #########delstopwords_result是处理后的结果
    delstopwords_result = codecs.open('key/pinglun_filter_all1.txt','w',encoding='utf-8')
    ############加载停用词
    for line in st:
        line = line.strip()
        stopwords.append(line)
    print (u'正在过滤停用词......')
    ###############
    for singletext_result in file:
        for word in singletext_result:
            if word in stopwords:
                word = ' '
            delstopwords_singletxt.append(word)
    delstopwords_alltxt.append(delstopwords_singletxt)
    for delstopwords_singletxt in delstopwords_alltxt:
        for everyword in delstopwords_singletxt:
            delstopwords_result.write(everyword)
        delstopwords_result.write('\n')
    delstopwords_result.close()
    print (u'保存文件为key/pinglun_filter1.txt！')
def run():
    filter()
if __name__ == '__main__':
    run()
