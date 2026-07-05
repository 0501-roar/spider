# 爬虫成长之路 · 项目2：爬取豆瓣图片

> 个人爬虫练习项目，用于学习 Python 网络爬虫基础。

## 📁 项目结构

```
项目2爬去豆瓣图片/
├── 爬去豆瓣图片.py      # 爬虫主程序
├── 爬取的图片1/         # 爬取到的图片资源
│   ├── img-1
│   ├── img-2
│   ├── ...
│   └── img-25
└── README.md            # 项目说明
```

## 🚀 功能说明

- 目标站点：豆瓣
- 抓取内容：图片资源
- 输出结果：将下载的图片保存到 `爬取的图片1/` 目录下

## 🛠 技术栈

- Python
- 网络请求（如 `requests`）
- 网页解析（如 `BeautifulSoup` / `lxml`）

## 📌 使用方式

1. 安装依赖（如有 `requirements.txt`）：
   ```bash
   pip install -r requirements.txt
   ```

2. 运行爬虫：
   ```bash
   python 爬去豆瓣图片.py
   ```

3. 查看结果：
   打开 `爬取的图片1/` 文件夹即可查看下载的图片。

## ⚠️ 免责声明

本项目仅作为个人学习和技术交流使用，请遵守目标网站的 [Robots 协议](https://www.douban.com/robots.txt) 及相关法律法规，勿用于商业用途或高频爬取。

## 🔗 GitHub 仓库

[https://github.com/0501-roar/spider](https://github.com/0501-roar/spider)

---

*Created by 0501-roar*
