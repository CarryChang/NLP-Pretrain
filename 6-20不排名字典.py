def cut_reverse():
    word_df = []
    #使用test
    # in_file = 'key/ltp_cu.txt'
    in_file = 'key/cut-938.txt'
    word_count = {}#统计词频的字典
    for line in open(in_file,'r',encoding='utf-8'):
        words = line.strip().split(" ")
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    for word in word_count.keys():
        if word:
            #按词频的顺序遍历字典的每个元素
            # print(word)
            word_df.append([word, str(word_count.get(word))])
        else:continue

if __name__ == '__main__':
    cut_reverse()