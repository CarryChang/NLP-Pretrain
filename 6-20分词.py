from pyltp import Segmentor
from pyltp import Postagger
def run():
    #分词+选词
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    cont = open('key/pinglun_resource.txt','r',encoding='utf-8')
    # cont = open('key/text.txt','r',encoding='utf-8')
    f = open('key/cut-938.txt','w',encoding='utf-8')
    segmentor = Segmentor()  # 初始化实例
    # segmentor.load('cws.model')  # 加载模型,不加载字典
    segmentor.load_with_lexicon('cws.model', 'userdict.txt') # 加载模型,加载用户字典
    postagger = Postagger() # 初始化实例
    postagger.load('pos.model')  # 加载模型
    for sentence in cont:
        if sentence.strip() !='':
            words = segmentor.segment(sentence)  # 分词
            postags = postagger.postag(words)  # 词性标注
            for word,tag in zip(words,postags):
                # if((tag == 'n'or tag == 'd' or tag == 'a') ):
                if((tag != 'wp' and tag != 'm' and tag != 'u' and tag!= 'q')):
                # if((tag == 'a' or tag == 'n') and len(word)>1):
                    f.write(word+' ')
            f.write('\n')
        else:continue
    f.close()
if __name__ == '__main__':
    import time
    starttime1=time.clock()
    run()
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)