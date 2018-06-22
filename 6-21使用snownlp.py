from snownlp import SnowNLP

#创建snownlp对象，设置要测试的语句
s = SnowNLP('虽然今天天气不错，但是我很不开心')
# 调用sentiments方法获取积极情感概率
print(s.sentiments)
from aip import AipNlp
""" 你的 APPID AK SK """
# 利用百度云提供的API接口实现情感分析
APP_ID = '10938200'
API_KEY = 'y11cG8tgPkL4m0BBsVAk84mw'
SECRET_KEY = '3FL7fm6zDaICROkNzcp3nOG2UGorugr0'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
# 使用百度api
print('connect successful')
texts = "虽然今天天气不错，但是我很不开心"
data = client.sentimentClassify(texts)
if data['items'][0]['positive_prob'] > data['items'][0]['negative_prob']:print('这句话情感积极')
else:print('这句话情感消极')
