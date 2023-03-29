# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/26  23:20
@Contact：473153250@qq.com
"""
import requests

# session = requests.session()
#
# HEADERS = {
#     'Host': 'www.researchgate.net',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'DNT': '1',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.researchgate.net',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1'
# }
#
# url = 'https://www.researchgate.net/publication/367224504_Role_of_Molecular_Symmetry_on_the_Magnetic_Relaxation_Dynamics_of_Five-Coordinate_DyIII_Complexes'
# resp = session.get(url, headers=HEADERS)
# print(resp)
from crawlerutils import ChromeBrowser
from crawlerutils import AuthorArtical as aa

obj = ChromeBrowser.ChromeBrowser()
with obj:
    chrome = obj.Browser
    aa.main(chrome, "https://www.researchgate.net/profile/Hu-Kongqiu")

# print('{:-^50}'.format('浏览器已关闭！'))