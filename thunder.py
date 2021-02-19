# -*- coding: utf-8 -*-
"""
@file: thunder.py
@time: 2021/2/19 12:26
@author:
@instruction: 
"""

class Thunder:
    agent = None

    def __init__(self):
        from win32com.client import Dispatch
        self.agent = Dispatch('ThunderAgent.Agent64.1')

    def download(self,filename,url):
        self.agent.AddTask(url, filename,nStartMode=1)

    def commit(self):
        """
        TODO: 每次提交任务都会弹出新建任务的面板，很烦，
        """
        self.agent.CommitTasks()

