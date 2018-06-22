from gensim.models import LdaModel
import gensim
lda = LdaModel.load('model/lda_gensim')
########使用ldaa进行聚类
for topic_id in range(10):
    print('Topic', topic_id)
    #####加上[0]表示提取主题，不加上则是输出全部主题
    print(lda.print_topics(topic_id))
    #print(lda.print_topics(topic_id)[0])输出每个类的第一个

