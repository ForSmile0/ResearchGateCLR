# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/25  19:43
@Contact：473153250@qq.com
"""
import yaml

with open('config.yml', 'r', encoding='utf-8') as f:
    globalConfig = yaml.load(f.read(), Loader=yaml.FullLoader)
# Author
