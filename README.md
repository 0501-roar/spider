# 🕷️ Spider · 豆瓣评论词云

> Python 爬虫入门练习：爬取豆瓣图书短评，并用 jieba + pyecharts 生成词云图。

---

## 📌 项目简介

本项目是爬虫学习过程中的第一个小练习，主要完成以下任务：

1. 使用 `requests` 请求豆瓣图书页面，并携带 `User-Agent` 头部模拟浏览器访问。
2. 使用 `BeautifulSoup` 提取页面中的短评内容。
3. 使用 `jieba` 对短评进行中文分词。
4. 使用 `pyecharts` 生成可交互的词云图，保存为 `ran.html`。

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/0501-roar/spider.git
cd spider
```

### 2. 安装依赖

```bash
pip install beautifulsoup4 requests jieba pyecharts lxml
```

### 3. 运行程序

```bash
python "爬取豆瓣网页，并且生成词云图.py"
```

运行成功后，打开生成的 `ran.html` 即可查看词云效果。

---

## 📂 文件说明

| 文件 | 说明 |
|------|------|
| `爬取豆瓣网页，并且生成词云图.py` | 主程序：爬取短评并生成词云 |
| `ran.html` | 运行后生成的词云图页面 |
| `README.md` | 项目说明文档 |

---

## 🛠️ 核心技术

- **requests** —— 发送 HTTP 请求
- **BeautifulSoup4** —— HTML 解析
- **jieba** —— 中文分词
- **pyecharts** —— 数据可视化 / 词云生成

---

## ⚠️ 注意事项

- 本项目仅供学习交流使用，请遵守豆瓣网站的 `robots.txt` 及相关使用条款。
- 建议控制请求频率，避免对目标网站造成过大压力。
- 豆瓣页面结构可能会更新，若解析失败，请检查短评对应的 HTML class 是否发生变化。

---

## 👤 作者

[0501-roar](https://github.com/0501-roar)
