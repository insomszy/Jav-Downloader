# -*- coding: utf-8 -*-
"""
@file: magnet.py
@time: 2021/2/19 12:43
@author:
@instruction: 
"""
from datetime import datetime, timedelta
import math


class Magnet:
    def __init__(self, title, size, date, pv, url):
        self.title = title
        self.size = size
        self.date = date
        self.pv = pv
        self.rate()
        self.url = url

    @staticmethod
    def date_score(date):
        date_diff = (datetime.now() - datetime.strptime(str(date), '%Y%m%d')).days
        d = 1 / ((math.log(((date_diff + 1000) / 365), math.e)) ** 1.5)
        return (round(d, 4))

    @staticmethod
    def size_score(size):
        return round((-size ** (-0.9) + 1) ** 1, 4)

    @staticmethod
    def pv_score(pv):
        return round((math.log(int(pv), math.e) / 10) ** 2, 4)

    def rate(self):
        self.score = 0
        if '-c' in self.title.lower():
            self.score += 1
        if self.date:
            self.score += self.date_score(self.date)
        if self.size:
            self.score += 2 * self.size_score(self.size)
        if self.pv:
            self.score += self.pv_score(self.pv)
