from aip import AipNlp
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import io
import sys
#改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# texts = "而且客栈离汽车站和火车站都非常近"
# data = client.sentimentClassify(texts)
# if data['items'][0]['positive_prob'] > data['items'][0]['negative_prob']:print('这句话情感积极')
# else:print('这句话情感消极')
def snowanalysis(key_word,client):
    print(key_word)
    sentiments_list = []
    print('正在执行...')
    key_txt = open('keywords/key_list/%s.txt'%key_word,'r',encoding='utf-8')
    key_txt_neg = open('keywords/emotion_1/%s_neg.txt'%key_word,'w',encoding='utf-8')
    key_txt_pos = open('keywords/emotion_1/%s_pos.txt'%key_word,'w',encoding='utf-8')
    for li in key_txt:
        s = client.sentimentClassify(li.encode('utf-8'))
        try:
            if s['items'][0]['positive_prob'] > s['items'][0]['negative_prob']:
                sentiments_list.append(s['items'][0]['positive_prob'])
                key_txt_pos.write(li)
            else: key_txt_neg.write(li)
            sentiments_list.append(1-s['items'][0]['negative_prob'])
        except Exception as e:
            pass
    plt.hist(sentiments_list, bins=np.arange(0, 1, 0.01))
    plt.xlabel("情感值")
    plt.ylabel("评论数目")
    plt.title(key_word+'-情感极性分布图')
    plt.show()

if __name__ == '__main__':
    APP_ID = '10938200'
    API_KEY = 'y11cG8tgPkL4m0BBsVAk84mw'
    SECRET_KEY = '3FL7fm6zDaICROkNzcp3nOG2UGorugr0'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    # 使用百度api
    print('connect successful')
    key_words = {'环境','娱乐','位置','价格','特色','设施','餐饮','交通','卫生','服务','体验'}
    for key_word in key_words:
        snowanalysis(key_word,client)