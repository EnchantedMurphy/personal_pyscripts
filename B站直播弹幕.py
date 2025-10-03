# -*- encoding: utf-8 -*-
#@time:  2020/11/15 22:54
#@author: chenTao
#@file:  dnmu.py
 
import requests
import time
import io,sys
# import
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
 
 
class Danmu():
    def __init__(self):
        # 弹幕url
        self.url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'
        # 请求头
        self.headers = {
            'Host': 'api.live.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        }
        # 定义POST传递的参数
        self.data = {
            'roomid': '21759012',
            'csrf_token': '',
            'csrf': '',
            'visit_id': '',
        }
 
    def get_danmu(self):
        # 获取直播间弹幕
        html = requests.post(url=self.url, headers=self.headers, data=self.data).json()
        # 解析弹幕列表
        for content in html['data']['room']:
            # 获取昵称
            nickname = content['nickname']
            # 获取发言
            text = content['text']
            # 获取发言时间
            timeline = content['timeline']
            # 记录发言
            msg = timeline + ' ' + nickname + ': ' + text
            print(msg)
 
if __name__ == '__main__':
    # 创建bDanmu实例
    bDanmu = Danmu()
    # 获取弹幕
    bDanmu.get_danmu()
 