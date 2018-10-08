from urllib.parse import urlencode
from download import save_to_txt
from utils import html_download
from parse import parse_content, parse_title
from settings import MAX_PAGE

def search(query, page, ranges='title', c='news',sort='time'):
    base_url = 'https://search.sina.com.cn/?'
    param = {
        'q' : query.encode('gb2312'),
        'range' : ranges,
        'c' : c,
        'sort' : sort,
        'page' : page
    }
    html = html_download(base_url + urlencode(param))
    for url in parse_title(html):
        yield url
    

def save(url):
    html = html_download(url, 'utf-8')
    title, contents = parse_content(html)
    save_to_txt(title, contents)


def main(query):
    for i in range(1, MAX_PAGE+1):
        for url in search(query, i):
            save(url)


if __name__ == '__main__':
    main('养猪')
