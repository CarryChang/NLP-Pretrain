def read(i,key_words):
    ############数字不用“”
    key_list = {0: '环境',
                1: '娱乐',
                2: '位置',
                }
    print(key_list[i]+'####################')
    for word in key_words:
        print(word)
if __name__ == '__main__':
    key_words_list = [{'环境','周边','周边环境','风景','空气','别墅','花园','街','镇','山谷','洋房','台阶','画廊','小区','海拔'},
                      {'演出'},
                      {'位置','地理','地图','中心','交通'},
                      ]
    i = 0
    for key_words in key_words_list:
        read(i,key_words)
        i += 1




