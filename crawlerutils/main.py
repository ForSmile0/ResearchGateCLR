# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/25  20:12
@Contact：473153250@qq.com
"""

from crawlerutils import ChromeBrowser as cb
from crawlerutils import AuthorArtical as aa
import csv


def getAuthorPaper(url: str):
    '''
    :param url: such as 'https://www.researchgate.net/profile/authorName'
    :return:
    '''
    obj = cb.ChromeBrowser()
    with obj:
        chrome = obj.Browser
        info = aa.main(chrome, url)
    with open(f"{url.split('/')[-1]}.csv", 'w', newline='', encoding='utf-8') as f:
        header = ['title', 'infoUrl', 'doi']  # 数据列名
        # encoding='utf-8'表示编码格式为utf-8，如果不希望在excel中打开csv文件出现中文乱码的话，将其去掉不写也行。
        writer = csv.DictWriter(f, fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        writer.writeheader()  # 写入列名
        writer.writerows(info)  # 写入数据


if __name__ == '__main__':
    getAuthorPaper('https://www.researchgate.net/profile/Lei-Mei')
