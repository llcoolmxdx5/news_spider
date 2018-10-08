import sys 
import os
# 文件存放路径 默认为程序执行目录+result
# 例: 程序文件在c:\新建文件夹\新建文件夹\crawl\新浪新闻\搜索\run.py
#     新闻文本存放路径为c:\新建文件夹\新建文件夹\crawl\新浪新闻\搜索\result
PATH = sys.path[0][:-4] + r'\result'
isExists = os.path.exists(PATH)
if not isExists:
    os.makedirs(PATH)
# 定义按关键词搜索的页数
MAX_PAGE = 10
# FLASK 配置
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 8888

