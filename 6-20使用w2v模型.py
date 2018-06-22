from gensim.models import Word2Vec
test = Word2Vec.load('model/word2vec_gensim')
data = test.most_similar_cosmul('房间')
for s in data:
    print("word:%s,similar:%s " %(s[0],s[1]))

