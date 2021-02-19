# -*- coding: utf-8 -*-
"""
@file: seed8.py
@time: 2021/2/19 14:03
@author:
@instruction: 2021/02/19 seed8存活确认
"""
from bt_site.html import HTML
import requests
import re
from magnet import Magnet
from thunder import Thunder


class Seed8(HTML):

    @classmethod
    def search(self, code):
        url = 'http://seed8.cc/search?wd=%s' % code
        r = requests.get(url=url)
        self.content = r.content.decode('utf-8')

    @classmethod
    def get_magnets(self):
        self.magnet_list = []

        for i in self.content.split('<li class="media">'):
            if '日期' in i:
                # print(i)
                date = re.search(r'日期：<span class="s_b">(.*?)</span>', i)[1].replace('-', '')
                size = re.search(r'大小：<span class="s_b">(.*?)</span>', i)[1]
                size = round((float(size.split(' ')[0])) / 1000 if 'gb' not in size.lower() else float(size.split(' ')[0]), 4)
                pv = re.search(r'点击：<span class="s_b">(.*?)</span>', i)[1]
                title = re.search(r'title="(.*?)"', i)[1]

                href = re.search(r'<a href="(.*?)"', i)[1]
                a = requests.get(url='http://seed8.cc%s' % href).content.decode('utf-8')
                url = 'magnet' + re.search(r'<a href="magnet(.*?)" id="down-url"', a)[1]

                m = Magnet(title, size, date, pv, url)
                self.magnet_list.append(m)

    @classmethod
    def get_torrent(self, code, order=0):
        self.search(code)
        self.get_magnets()
        self.magnet_list = sorted(self.magnet_list, key=lambda m: -m.score)
        magnet = self.magnet_list[order]
        print(code, magnet.title, magnet.size, magnet.date, magnet.pv)
        return magnet.title, magnet.url
