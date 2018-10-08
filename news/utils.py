import requests

def html_download(url, encoding='gb2312'):
    headers = {'User-Agent': "User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
    # request = Request(url, headers=headers)
    try:
        html = requests.get(url, headers=headers, timeout=(5, 18))
        html.encoding = encoding
    except:
        print('错误', url)
    else:
        return html.text
