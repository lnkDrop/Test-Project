#!/usr/bin/env python
# -*- coding:utf-8 -*-


import csv

f1 = csv.reader(open("四六级单词.csv", "r"))  # 读取四六级单词文件obj f1

# print(rd)
x = 0
data1 = []


def cigen():
    data2 = []
    shiyi = []
    f2 = open('词根.txt', 'r')  # 读取词根文件obj f2
    rd = f2.readline()  # 逐行读取词根
    for cigen in range(617):
        # print(rd.split())
        if rd.split() != []:
            shiyi.append(rd)
            # print(rd.split()[0])  # 提取词根单词用于匹配(不包含释义)
            data2.append(rd.split()[0])
        rd = f2.readline()
    f2.close()
    return data2


def shiyi():
    shiyi = []
    f2 = open('词根.txt', 'r')  # 读取词根文件obj f2
    rd = f2.readline()  # 逐行读取词根
    for cigen in range(617):
        # print(rd.split())
        if rd.split() != []:
            shiyi.append(rd)
        rd = f2.readline()
    f2.close()
    return shiyi

# 逐行读取单词
for danci in f1:
    data1.append(danci)
    x += 1  # 记录行数

j = 0
while j < x:
    # print(data1[j][0],data1[j][1])       #每次循环提取一条单词记录
    for i in range(300):
        # print(cigen())
          # 每次提取所有词根，用来对比
        if cigen()[i] in data1[j][0]:     #如果匹配成功，重置词根，单词跳转到下一条
            print("单词: "+str(data1[j][0])+" "+str(data1[j][1])+"    词根："+str(shiyi()[i]))

    j += 1
