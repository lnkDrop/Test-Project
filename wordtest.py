#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 获取四六级真题的单词，和词频的统计（字典方式）
import docx
import re
import os

def getword():
    dict = {}
    file_path = []
    path = r"D:/Project/真题数据源/"
    for filename in os.listdir(path):  # 获取path下所有文件的路径
        file_path.append((os.path.join(path, filename)))
    for i in range(len(file_path)):
        f = docx.Document(file_path[i])  # 读取四六级真题
        for para in f.paragraphs:
            txt = para.text
            result_list = re.findall(r'[a-zA-Z]+', txt)  # 正则表达式提取出英文单词
            for key in result_list:
                dict[key] = dict.get(key, 0) + 1  # 把出现的单词放入字典，按出现次数进行词频统计
    print(dict)  # 查看词频
    print(len(dict))  # 查看单词总数


getword()
