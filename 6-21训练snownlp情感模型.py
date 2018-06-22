from snownlp import sentiment
sentiment.train('train/neg.txt', 'train/pos.txt')
sentiment.save('train/sentiment.marshal')