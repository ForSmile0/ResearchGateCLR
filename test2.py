# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/27  21:40
@Contact：473153250@qq.com
"""
import sys

import time


def progress_bar(num):
    for i in range(1, num+1):
        print("\r", end="")
        print("Download progress: {}/{}: ".format(i, num), "▋" * i, end="")
        sys.stdout.flush()
        time.sleep(0.5)


if __name__ == '__main__':
    print(123)
    progress_bar(56)
