import re
import json

import re
def azlist():
    List = []
    for ch in range(97, 123):
        List += chr(ch)
    return List

num = azlist()



# 读取单词
file = open('data/testDiction.txt', 'r')
file2 = open('data/testRoot.txt', 'r')
js = file.read()
dic = json.loads(js)
danci = []
for key in dic:
    # print(key)
    danci.append(key)
file.close()
# print(danci)

for i in range(len(num)):
    f = open(r"D:/Project/Root_Diction/"+str(num[i])+".txt", 'r', encoding='utf-8')
    lines = f.readlines()
    RD = []
    for line3 in lines:
        if line3[0:4] == "【词根】":
            result_list = re.findall('[a-zA-Z]+', line3)  # 正则表达式取出词根
            if len(result_list) and result_list[0].startswith(num[i]):
                # print(result_list)
                RD += list(set(result_list))
                # print(result_list)
                for j in range(len(result_list)):         #提取单个待匹配词根
                    if len(result_list[j]) > 1:             #过滤单单词数据("a","b","c"....)
                        # print(result_list[j])
                        for z in range(len(danci)):         #取出单个单词准备一一比较
                            if result_list[j] in danci[z]:         #比较该词根是否存在与单词中
                                # print(danci[z][0:len(result_list[j])])
                                print("单词:" + str(danci[z]) + "    词根:" + str(result_list[j]))

                                # if result_list[j] == danci[z][0:(len(result_list[j]))]:      #比较前后缀(未完善)
                                #     print("单词:" + str(danci[z]) + "    前缀:" + str(result_list[j]))
                                # elif result_list[j] == danci[z][-(len(result_list[j])):]:
                                #     print("单词:" + str(danci[z]) + "    后缀:" + str(result_list[j]))
                                # else:
                                #     print("单词:" + str(danci[z]) + "    词根:" + str(result_list[j]))
