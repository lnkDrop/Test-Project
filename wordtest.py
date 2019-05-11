#!/usr/bin/env python
# -*- coding:utf-8 -*-

import docx
import re

f = docx.Document(r"D:/Project/真题数据源/2013061.docx") #读取四六级真题
dict = {}
for para in f.paragraphs:
    txt = para.text
    result_list = re.findall(r'[a-zA-Z]+', txt)   #正则表达式提取出英文单词
    for key in result_list:
        dict[key] = dict.get(key, 0) + 1        #把出现的单词放入字典，按出现次数进行词频统计
print(dict)

# x = ['a','a','b','c','c','c']
# for key in x:
#     dict[key] = dict.get(key, 0)+1
# print(dict)