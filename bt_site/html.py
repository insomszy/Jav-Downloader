# -*- coding: utf-8 -*-
"""
@file: html.py
@time: 2021/2/19 13:58
@author:
@instruction:
"""
import abc


class HTML:
    @abc.abstractmethod
    def search(self, code):
        """
        给定关键字 出搜索结果
        :param code: 神秘代码
        """
        pass

    @abc.abstractmethod
    def get_magnets(self):
        """
        解析搜索结果里的种子
        """
        pass

    @abc.abstractmethod
    def get_torrent(self, code, order=0):
        """
        获取最终下载链接
        """
        pass
