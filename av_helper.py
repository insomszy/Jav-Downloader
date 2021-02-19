# -*- coding: utf-8 -*-
"""
@file: av_helper.py
@time: 2021/2/19 14:52
@author:
@instruction: 
"""
from bt_site.seed8 import Seed8
from thunder import Thunder

thunder = Thunder()
bt = Seed8()

with open('logs/done', 'w') as e, open('logs/to_do', 'r') as f, open('logs/redo', 'w') as g:
    for code in f.readlines():
        code = code.strip()
        try:
            title, url = bt.get_torrent(code)
        except IndexError: # 查无此片
            g.write(code + '\n')
            continue
        thunder.download(title, url)
        e.write('{}\n{} {}'.format(code, title, url))

thunder.commit()
