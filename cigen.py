#!/usr/bin/env python
# -*- coding:utf-8 -*-


f = open('词根.txt', 'r')
rd = f.readline()
# print(rd)
s = []
for i in range(617):
    # print(rd.split())
    if rd.split() != []:
        print(rd)       #提取词根单词用于匹配(不包含释义)
        # if rd.split()[0] in
    rd = f.readline()