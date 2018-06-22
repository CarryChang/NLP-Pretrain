from pyltp import Segmentor
from pyltp import Postagger
def run():
    #分词+去除空行
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    cont = open('key/pinglun_resource.txt','r',encoding='utf-8')
    # cont = open('key/text.txt','r',encoding='utf-8')
    f = open('key/cut_resouce_new.txt','w',encoding='utf-8')
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
                if (tag !='wp'):
                    f.write(word+' ')
                else:f.write('\n')
            f.write('\n')
        else:continue
    f.close()
def rewrite():
    #分词+去除空行
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    # cont = open('key/pinglun_resource.txt','r',encoding='utf-8')
    cont = open('key/cut_resouce_new.txt','r',encoding='utf-8')
    f = open('key/pure_cut_final_new.txt','w',encoding='utf-8')
    for sentence in cont:
        if sentence.strip() !='':
            f.write(sentence)
        else:continue
    f.close()
if __name__ == '__main__':
    import time
    starttime1=time.clock()
    run()
    rewrite()
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)