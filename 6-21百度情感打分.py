from aip import AipNlp
""" 你的 APPID AK SK """
# 利用百度云提供的API接口实现情感分析
APP_ID = '10938200'
API_KEY = 'y11cG8tgPkL4m0BBsVAk84mw'
SECRET_KEY = '3FL7fm6zDaICROkNzcp3nOG2UGorugr0'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
# 使用百度api
print('connect successful')
texts = {"顺便说一句，景区的高空玻璃平台千万别去，有点上当的感觉！",
        '服务不够。',}

for text in texts:
    data = client.sentimentClassify(text)
    if data['items'][0]['positive_prob'] > data['items'][0]['negative_prob']:
        print('这句话情感积极')
        #######使用映射
        print(dict['这句话情感积极'])
    else:print('这句话情感消极')
    print(dict['这句话情感消极'])




