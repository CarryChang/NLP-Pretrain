def cut_reverse():
    word_df = []
    # in_file = 'key/ltp_cu.txt'
    in_file = 'result/pure_n.txt'
    word_count = {}#统计词频的字典
    for line in open(in_file,'r',encoding='utf-8'):
        words = line.strip().split(" ")
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    for word in word_count.keys():
        ##############选择字数大于1的挑出来
        if word:
            word_df.append([word, str(word_count.get(word))])
        else:continue
    with open("result/pure_n_reverse_new.txt", 'w',encoding='utf-8') as wf2:
        word_df.sort(key=lambda x: int(x[1]),reverse=True)
        wf2.truncate()
        for item in word_df:
            for word in item:
                wf2.write(word + ' ')
            wf2.write('\n')
        print('字典倒序排序已经成功 ')
    wf2.close()
if __name__ == '__main__':
    cut_reverse()