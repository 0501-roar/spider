import requests
from bs4 import BeautifulSoup
url="https://movie.douban.com/top250"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"}
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,"lxml")
content_all=soup.find_all(name="div",class_="item")
imgList=[]
for content in content_all:
    contentImg=content.find(name="img")
    if contentImg:
        imgurl=contentImg["src"]
        imgList.append(imgurl)
    else:
        print("你的找img的url那步返回了None")
n=0
for img in imgList:
    n+=1
    response=requests.get(img,headers=headers)
    content_img=response.content
    with open(f"D:\\编程练习-Code\\Python练习\\python爬虫练习\\爬虫成长之路\\项目2爬去豆瓣图片\\爬取的图片1\\img-{n}","wb") as f:
        f.write(content_img)
print("success")