# -*- coding: UTF-8 -*-

import requests
import setting
import time
import re
import random

def spider():
    i = 0
    pageList = []

    # 获取全部每日新闻页面 URL
    while True:
        i += 1
        if i == 2:
            break
        url = setting.url + str(i)
        pageHtml = requests.get(url = url, headers = setting.headers)
        pageList += re.compile('</i><a href="(.+?)" title=').findall(pageHtml.text)
        time.sleep(random.randint(1,5))
    
    # 爬取页面的内容
    for pageURL in pageList:
        time.sleep(random.randint(1,5))
        pageHtml = requests.get(url = pageURL, headers = setting.headers)
        headlines = re.compile(r"<li>(.+?)</li>").findall(pageHtml.text)
        # print(headlines)
        
        headlines = [i for i in headlines if i.find(r"</a>") == -1]     # 去除脏数据
        newsContent = re.compile(r"<p>(.+?)</p>").findall(pageHtml.text)
        f = open(r"E:\code\python\newsCrawler\a.txt", "w+", encoding = "utf-8")
        for i in newsContent:
            i = re.compile(r"(<strong>)|(</strong>)|(<br/>)|<br />|(<span(.+?)</span>)").sub("", i)
            i = re.compile(r"&ldquo;").sub("“", i)
            i = re.compile(r"&rdquo;").sub("”", i)
            i = re.compile(r"&middot;").sub("·", i)
            i = re.compile(r"&mdash;").sub("—", i)
            # i.replace(r"<strong>""</strong>", "")
            f.write(i + "\r\n")
        f.close()
        # f = open(r"E:\code\python\newsCrawler\a.txt", "w+", encoding = "utf-8")
        # for i in headlines:
        #     if i.find(r"</a>") != -1:   # 去除脏数据
        #         print(i)
        #         headlines.remove(i)
        # f.close()
if __name__ == "__main__":
    spider()
