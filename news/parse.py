import re
import logging
from pyquery import PyQuery as pq
from download import save_to_txt


def parse_content(html):
    # regexp = r'<meta name="tags" content="(.*?)" />'
    # keyword = re.findall(regexp, html)
    doc = pq(html)
    title = doc('h1').text()
    try:
        content = doc('.article p').text()
        if not content:
            content = doc('.content p').text()
        if not content:
            content = doc('#artibody p').text()
    except Exception as e:
        logging.warning("[P] 解析网页内容失败: %s" % e)
    # img_urls = []
    # for item in doc('.img_wrapper img').items():
    #     img_urls.append(item.attr.src)
    # contentl = content.split(' ')
    return title,content

def parse_title(html):
    doc = pq(html)
    urls = doc('h2 a').items()
    for url in urls:
        yield url.attr.href


if __name__ == '__main__':
    pass







