#!/usr/bin/env python
# -*- coding:utf-8 -*-

qianzhui = []
f = open("data/前缀.txt",'r')
rd = f.readline()
for cigen in range(275):
    # print(rd.split())
    if rd.split() != []:
        # print(rd.split()[0])  # 提取前缀用于匹配(不包含释义)
        print(rd)
    rd = f.readline()
f.close()
