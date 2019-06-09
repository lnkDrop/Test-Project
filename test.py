# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # @Name: 杨钦凯
# # @Student ID:20161152105
# # @File  : test.py
# # coding=utf-8
# '''
# Created on 2018.8.18
# @author: ZEC---
# '''
#
# import requests
# import pymysql
# from bs4 import BeautifulSoup
#
#
# def insert(english, chinese, imgurl):
#     db = pymysql.connect("localhost", "3306", "root", "123456", "test")
#     cursor = db.cursor()
#     # summary = summary.tostring(summary,encoding='utf-8')
#     english = pymysql.escape_string(english)
#     chinese = pymysql.escape_string(chinese)
#     imgurl = pymysql.escape_string(imgurl)
#     sql = "insert into reaserchwords(english,chinese,\
#     imgurl) values('" + english + "','" + chinese + "','" + imgurl + "')"
#
#     cursor.execute(sql)
#     db.commit()
#     db.close()
#
#
# def transurl(url):
#     url = "http://www.youdict.com" + url
#     url.strip('\n')
#     return url
#
#
# def main_thread(start, end):
#     i = start
#     while i < end:
#         newsurl = 'http://www.youdict.com\
#         /ciku/id_5_0_0_0_' + str(i) + '.html'
#         res = requests.get(newsurl)
#         # res=requests.get(newsurl)
#         res.encoding = 'utf-8'
#         soup = BeautifulSoup(res.text, 'html.parser')
#         # print(soup)
#         divs = soup.select(".col-sm-6")
#         # print(divs[0])
#         for each_div in divs:
#             english = each_div.div.div.h3.a.text
#             imgurl = transurl(each_div.div.img['src'])
#             chinese = each_div.div.p.text
#             # print(english+"   "+imgurl+"  "+chinese)
#             insert(english, chinese, imgurl)
#         print(str(i + 1) + "页面 is ok")
#         i = i + 1
#
#
# main_thread(67, 274)
a = "asdfgh"
b = "sd"
print(a[-3:])

