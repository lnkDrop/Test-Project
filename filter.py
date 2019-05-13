import re
import json

class DB:
    def __init__(self, Root, text, num):
        self.Root = Root         #词根
        self.text = text         #单词
        self.num = num           #遍历首字母

    # 读取单词
    def readtxt(self):
        file = open('testDiction.txt', 'r')
        js = file.read()
        dic = json.loads(js)
        print(dic)
        return dic
        file.close()

    # 将爬取的词根单独提取出来以用作搜索
    # def Root_Diction(self):
    #

    # 用词根搜索单词的正则匹配函数（模糊查询）
    # def fuzzyfinder(self):
    #     suggestions = []
    #     pattern = '.*'.join(self.Root)  # 转换 'abc' to 'a.*b.*c'
    #     regex = re.compile(pattern)
    #     for item in self.text:
    #         match = regex.search(item)
    #         if match:
    #             suggestions.append(item)
    #     return suggestions
    # print(fuzzyfinder())
    # dict = readtxt()





