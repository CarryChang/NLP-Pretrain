from gensim.models import Word2Vec
import codecs
model = Word2Vec.load('model/word2vec_gensim')
# keywords = {'环境','周边','风景','景点','空气','花园','别墅'}
# keywords = {'位置','地理','地图','中心','交通'}
# keywords = {'特色','气息','建筑','结构','视线','江水','码头','风情'}
# keywords = {'设施','房间','硬件','客房','风格','信号'}
# keywords = {'风味','餐饮','菜品','味道','饭菜','水果','特产'}
keywords = {'价格'}
for word in keywords:
    try:
        print('#####model.most_similar(%s,topn=5)#####'%word)
        print(word)
        sim = model.most_similar(word,topn=30)
        for s in sim:
            print ("word:%s,similar:%s " %(s[0],s[1]))
    except Exception as e:
        pass


