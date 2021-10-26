# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/26 14:42
# @Copyright：北京码同学网络科技有限公司

# 这里封装发起请求的客户端对象
import requests
class RequestsClient:
    def __init__(self):
        # session对象是可以替代下面你看到的那些请求方式的
        """
        requests.get #发起get
        requests.post #发起post
        requests.put #发起put
        requests.delete #发起delete
        """
        # session对象是可以自动化管理整个cookie对象
        self.session = requests.session()
    def send(self,**kwargs):
        return self.session.request(**kwargs)

