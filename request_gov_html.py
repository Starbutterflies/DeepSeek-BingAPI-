import requests
import re
from lxml.html import fromstring, tostring

import re


from lxml.html import fromstring, tostring
from lxml.html.clean import Cleaner

def clean_html_lxml(html_text):
    cleaner = Cleaner(
        scripts=True,          # 删除脚本
        style=True,            # 删除样式
        comments=True,         # 删除注释
        embedded=True,         # 删除嵌入式内容（如Flash）
        links=True,            # 删除链接标签（保留文本）
        meta=True,             # 删除meta标签
        page_structure=False,  # 保留基本结构（如div/p）
        safe_attrs_only=True,   # 只保留安全属性（如href/src）
    )
    doc = fromstring(html_text)
    cleaned = cleaner.clean_html(doc)
    return tostring(cleaned, encoding="unicode")




HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://cn.bing.com/',
}


def request_html(url,timeout = 10):
    try:
        html = requests.get(url, headers=HEADERS,timeout=timeout)
        try:
            return html.content.decode("gbk")
        except:
            return html.content.decode("utf8")
    except:
        return None


if __name__ == '__main__':
    print(len(clean_html_lxml(request_html(r"http://www.tjcn.org/tjgb/16hn/36705.html"))))