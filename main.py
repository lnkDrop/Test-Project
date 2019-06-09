#!/usr/bin/env python
# -*- coding:utf-8 -*-


import csv
import unittest
f1 = csv.reader(open("data/四六级单词.csv", "r"))  # 读取四六级单词文件obj f1

# print(rd)
x = 0
data1 = []


def cigen():
    data = []
    f = open('data/词根.txt', 'r')  # 读取词根文件
    rd = f.readline()  # 逐行读取词根
    for cigen in range(617):
        # print(rd.split())
        if rd.split() != []:
            # print(rd.split()[0])  # 提取词根单词用于匹配(不包含释义)
            data.append(rd.split()[0])
        rd = f.readline()
    f.close()
    return data


def shiyi():
    shiyi = []
    f = open('data/词根.txt', 'r')  # 读取词根文件
    rd = f.readline()  # 逐行读取词根
    for cigen in range(617):
        # print(rd.split())
        if rd.split() != []:
            shiyi.append(rd)  # 词根带释义
        rd = f.readline()
    f.close()
    return shiyi


def qianzhui():
    qianzhui = []
    f = open("data/前缀.txt", 'r')
    rd = f.readline()
    for cigen in range(276):
        # print(rd.split())
        if rd.split() != []:
            # print(rd.split()[0])  # 提取前缀用于匹配(不包含释义)
            qianzhui.append(rd.split()[0])
        rd = f.readline()
    f.close()
    return qianzhui


def qiansy():
    shiyi = []
    f = open('data/前缀.txt', 'r')  # 读取前缀文件
    rd = f.readline()  # 逐行读取前缀
    for cigen in range(276):
        # print(rd.split())
        if rd.split() != []:
            shiyi.append(rd)  # 前缀带释义
        rd = f.readline()
    f.close()
    return shiyi


def houzhui():
    houzhui = []
    f = open("data/后缀.txt", 'r')
    rd = f.readline()
    for cigen in range(377):
        # print(rd.split())
        if rd.split() != []:
            # print(rd.split()[0])  # 提取后缀用于匹配(不包含释义)
            houzhui.append(rd.split()[0])
        rd = f.readline()
    f.close()
    return houzhui


def housy():
    houzhui = []
    f = open("data/后缀.txt", 'r')
    rd = f.readline()
    for cigen in range(377):
        # print(rd.split())
        if rd.split() != []:
            # print(rd.split()[0])  # 提取后缀用于匹配(不包含释义)
            houzhui.append(rd)
        rd = f.readline()
    f.close()
    return houzhui


# 逐行读取单词

for danci in f1:
    data1.append(danci)
    x += 1  # 记录行数

j = 0
while j < x:
    # print(data1[j][0],data1[j][1])       #每次循环提取一条单词记录
    for i in range(300):
        # print(cigen())
        # 提取词根，用来对比
        # print(data1[j][0][0:len(qianzhui()[i])])
        if cigen()[i] in data1[j][0]:  # 匹配
            print("单词: " + str(data1[j][0]) + " " + str(data1[j][1]) )
            print("  词根：" + str(shiyi()[i]))
            for qian in range(len(qianzhui())):  # 提取前缀，对比
                # print(qianzhui()[qian])
                if qianzhui()[qian] == data1[j][0][0:len(qianzhui()[qian])]:
                    print("  前缀: " + str(qiansy()[qian]))

            for hou in range(len(houzhui())):  # 提取后缀，对比
                # print(qianzhui()[qian])
                if houzhui()[hou] == data1[j][0][-len(houzhui()[hou]):]:
                    print("  后缀: " + str(housy()[hou]))

    j += 1

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(cigen("testSize"))
    suite.addTest(danci("testResize"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)