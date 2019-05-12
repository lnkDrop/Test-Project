import re
import json
#将爬取的词根单独提取出来以用作搜索
f = open(r"D:/Project/Root_Diction/a.txt", 'r', encoding='utf-8')
lines = f.readlines()
RD = []
for line3 in lines:
    if line3[0:4] == "【词根】":
        result_list = re.findall('[a-zA-Z]+', line3)
        if len(result_list) and result_list[0].startswith('a'):
            # print(result_list)
            RD += list(set(result_list))

# print(RD)
f.close()

def readtxt():
    file = open('test.txt', 'r')
    js = file.read()
    dic = json.loads(js)
    print(dic)
    return dic
    file.close()
#用词根搜索单词的正则匹配函数
def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*'.join(user_input)  # 转换 'abc' to 'a.*b.*c'
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append(item)
    return suggestions
# print(fuzzyfinder('ac',RD))

# dict = readtxt()
print()
