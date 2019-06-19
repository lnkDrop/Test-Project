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
    # 逐行读取词根
    count = len(f.readlines())
    f.close()
    f = open('data/词根.txt', 'r')
    for i in range(count):
        # print(rd.split())
        rd = f.readline()
        if rd.split() != []:
            # print(rd.split()[0])  # 提取词根单词用于匹配(不包含释义)
            data.append(rd.split()[0])
    f.close()

    for x in range(len(data) - 1):
        maxIndex = x
        for y in range(x + 1, len(data)):
            if len(str(data[y])) > len(str(data[maxIndex])):
                maxIndex = y
        data[x], data[maxIndex] = data[maxIndex], data[x]

    return data


cigen = cigen()


def shiyi():
    data = []
    f = open('data/词根.txt', 'r')  # 读取词根文件
    count = len(f.readlines())
    f.close()
    f = open('data/词根.txt', 'r')
    for i in range(count):
        # print(rd.split())
        rd = f.readline()  # 逐行读取词根
        rd = rd.strip('\n')  #去换行符
        if rd.split() != []:
            data.append(rd)  # 词根带释义
    f.close()

    for x in range(len(data) - 1):
        maxIndex = x
        for y in range(x + 1, len(data)):
            if len(str(data[y]).split()[0]) > len(
                    str(data[maxIndex]).split()[0]):
                maxIndex = y
        data[x], data[maxIndex] = data[maxIndex], data[x]
    # print(data)
    return data


shiyi = shiyi()
# print(shiyi())


def qianzhui():
    data = []
    f = open("data/前缀.txt", 'r')
    count = len(f.readlines())
    f.close()
    f = open('data/前缀.txt', 'r')
    for i in range(count):
        rd = f.readline()
        rd = rd.strip('\n')
        # print(rd.split())
        if rd.split() != []:
            # print(rd.split()[0])  # 提取前缀用于匹配(不包含释义)
            data.append(rd.split()[0])

    f.close()
    for x in range(len(data) - 1):
        maxIndex = x
        for y in range(x + 1, len(data)):
            if len(str(data[y]).split()[0]) > len(
                    str(data[maxIndex]).split()[0]):
                maxIndex = y
        data[x], data[maxIndex] = data[maxIndex], data[x]
    return data


qianzhui = qianzhui()


def qiansy():
    data = []
    f = open('data/前缀.txt', 'r')  # 读取前缀文件
    count = len(f.readlines())
    f.close()
    f = open('data/前缀.txt', 'r')
    # 逐行读取前缀
    for i in range(count):
        rd = f.readline()
        rd = rd.strip('\n')
        # print(rd.split())
        if rd.split() != []:
            data.append(rd)  # 前缀带释义

    f.close()
    for x in range(len(data) - 1):
        maxIndex = x
        for y in range(x + 1, len(data)):
            if len(str(data[y]).split()[0]) > len(
                    str(data[maxIndex]).split()[0]):
                maxIndex = y
        data[x], data[maxIndex] = data[maxIndex], data[x]
    return data


qiansy = qiansy()


def houzhui():
    data = []
    f = open("data/后缀.txt", 'r')
    count = len(f.readlines())
    f.close()
    f = open("data/后缀.txt", 'r')
    for i in range(count):
        rd = f.readline()
        rd = rd.strip('\n')
        # print(rd.split())
        if rd.split() != []:
            # print(rd.split()[0])  # 提取后缀用于匹配(不包含释义)
            data.append(rd.split()[0])

    f.close()
    for x in range(len(data) - 1):
        maxIndex = x
        for y in range(x + 1, len(data)):
            if len(str(data[y]).split()[0]) > len(
                    str(data[maxIndex]).split()[0]):
                maxIndex = y
        data[x], data[maxIndex] = data[maxIndex], data[x]
    return data


houzhui = houzhui()


def housy():
    data = []
    f = open("data/后缀.txt", 'r')
    f = open("data/后缀.txt", 'r')
    count = len(f.readlines())
    f.close()
    f = open("data/后缀.txt", 'r')
    for i in range(count):
        rd = f.readline()
        rd = rd.strip('\n')
        # print(rd.split())
        if rd.split() != []:
            # print(rd.split()[0])  # 提取后缀用于匹配(不包含释义)
            data.append(rd)

    f.close()
    for x in range(len(data) - 1):
        maxIndex = x
        for y in range(x + 1, len(data)):
            if len(str(data[y]).split()[0]) > len(
                    str(data[maxIndex]).split()[0]):
                maxIndex = y
        data[x], data[maxIndex] = data[maxIndex], data[x]
    return data


housy = housy()
# print(cigen)
# print(shiyi)
# 逐行读取单词

for danci in f1:
    data1.append(danci)
    x += 1  # 记录行数

j = 0
i = 0

while j < x:
    # print(data1[j][0],data1[j][1])       #每次循环提取一条单词记录
    for i in range(len(cigen)):
        # print(cigen()) 
        # 提取词根，用来对比
        # print(data1[j][0])
        # print(cigen()[i])
        if cigen[i] in data1[j][0]:  # 匹配
            print("单词: " + str(data1[j][0]) + " " + str(data1[j][1]))
            print("  词根："  + str(shiyi[i]))

            for qian in range(len(qianzhui)):  # 提取前缀，对比
                # print(qianzhui()[qian])
                if qianzhui[qian] == data1[j][0][0:len(qianzhui[qian])] and qianzhui[qian] not in cigen[i] and cigen[i] not in qianzhui[qian]:
                    print("  前缀: " + str(qiansy[qian]))
                    break

            for hou in range(len(houzhui)):  # 提取后缀，对比
                # print(qianzhui()[qian])
                if houzhui[hou] == data1[j][0][-len(houzhui[hou]):] and houzhui[hou] not in cigen[i] and cigen[i] not in houzhui[hou]:
                    print("  后缀: " + str(housy[hou]))
                    break
            print()
            j += 1
            continue
        
    j += 1
