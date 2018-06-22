# coding=utf-8
from aip import AipNlp
import codecs
""" 你的 APPID AK SK """
# 利用百度云提供的API接口实现情感分析
APP_ID = '10938200'
API_KEY = 'y11cG8tgPkL4m0BBsVAk84mw'
SECRET_KEY = '3FL7fm6zDaICROkNzcp3nOG2UGorugr0'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
# 使用百度api
print('connect successful')
# key_txt = open('C:/Users/63011/Desktop/重庆市乡村民宿满意度分析/keywords/key_list/keywords/key_list/env.txt', 'r')
# for text in key_txt:
#     print(text)
text = '今天天气不错，但是我不开心'
data = client.sentimentClassify(text)
print(data)

# texts = {"顺便说一句，景区的高空玻璃平台千万别去，有点上当的感觉！",
#         '服务不够。',}
# dict = {'这句话情感积极' : '1',
#         '这句话情感消极' : '0',
# }
# for text in texts:
#     data = client.sentimentClassify(text)
#     print(data)#sentiment:0表示消极，1表示中性，2表示积极
#     if data['items'][0]['positive_prob'] > data['items'][0]['negative_prob']:
#         print('这句话情感积极')
#         #######使用映射
#         print(dict['这句话情感积极'])
#     else:print('这句话情感消极')
#     print(dict['这句话情感消极'])




