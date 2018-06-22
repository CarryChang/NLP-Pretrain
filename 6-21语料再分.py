def run():
    #分词+去除空行
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    # cont = open('key/pinglun_resource.txt','r',encoding='utf-8')
    cont = open('key/cut_resouce.txt','r',encoding='utf-8')
    f = open('key/pure_cut_final.txt','w',encoding='utf-8')
    for sentence in cont:
        if sentence.strip() !='':
            f.write(sentence)
        else:continue
    f.close()
if __name__ == '__main__':
    import time
    starttime1=time.clock()
    run()
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)