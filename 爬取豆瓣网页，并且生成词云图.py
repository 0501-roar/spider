from bs4 import BeautifulSoup
import requests
import jieba
from pyecharts.charts import WordCloud
url="https://book.douban.com/subject/37843237/?icn=index-latestbook-subject"
# 伪装headers
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"}
response=requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "lxml")
content_all = soup.find_all(class_="short-content")
contentString1=[]
for content in content_all:
    p=content.find(name="p")
    if p:
        p.decompose()
    contentString1.append(content.text)
words=""
for wordd in contentString1:
    words+=wordd
wordds=jieba.lcut(words)
dict_words={}
for word in wordds:
    if len(word)>2:
        if word not in dict_words:
            dict_words[word]=1
        else:
            dict_words[word]+=1
wd=WordCloud()
wd.add(series_name="无",data_pair=dict_words.items(),word_size_range=[20,80])
wd.render("ran.html")