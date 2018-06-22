def read(number,key_words):
    key_list = {0: '环境',
                1: '娱乐',
                2: '位置',
                3: '价格',
                4: '特色',
                5: '设施',
                6: '餐饮',
                7: '交通',
                8: '卫生',
                9: '服务',
                10: '体验',
                }
    f = open('key/pure_cut_final.txt','r',encoding='utf-8')
    key_txt = open('keywords/key_list/%s.txt'%key_list[number],'w',encoding='utf-8')
    for sentence in f:
        for i in key_words:
            if i in sentence:
               key_txt.write(sentence)
            else:continue
    f.close()
    key_txt.close()
    print(key_list[number]+'已经查找完成')
if __name__ == '__main__':
    import time
    starttime1=time.clock()
    key_words_list = [{'环境','周边','周边环境','风景','空气','别墅','花园','街','镇','山谷','周围'},
                      {'娱乐','演出'},
                      {'位置','地理','地图','中心','交通','海拔'},
                      {'价格','房价','性价比','价位','单价'},
                      {'特色','特色','气息','建筑','结构','视线','江水','码头','风情','木楼','古城','隔音','游船','古镇','人情','别墅','画廊','洋房'},
                      {'设施','房间','硬件','客房','风格','信号','暖气','床','电热毯','热水','露台','阳台','空调','窗户'},
                      {'餐饮','风味','餐饮','菜品','味道','饭','菜','水果','特产','餐','早餐','烧烤','宵夜'},
                      {'交通','火车站','客运站','路程','停车','桥','路','景区','车站'},
                      {'卫生','气味','卫生状况','干净'},
                      {'服务','态度','服务态度','前台','服务员','老板','掌柜','店家'},
                      {'体验','整体','感觉'},
                      ]
    i = 0
    for key_words in key_words_list:
        read(i,key_words)
        i += 1
    endtime1=time.clock()
    T1=endtime1-starttime1
    print('总用时间为(单位s)：%s'%T1)