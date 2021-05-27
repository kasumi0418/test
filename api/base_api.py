# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/26 14:49
# @Copyright：北京码同学网络科技有限公司
import jsonpath

from common.client import RequestsClient


class BaseApi:
    token = None

    """
    BaseApi作为所有单接口的父类出现，将所有接口公共的属性或者方法信息进行抽象封装
    """
    def __init__(self):
        self.client = RequestsClient()
        self.host = "https://qyapi.weixin.qq.com"
        self.url =None
        self.method = None
        self.headers = None
        self.data = None
        self.params =None
        self.json = None
        self.resp = None
    def send(self,**kwargs): #**kwargs 表示接口在发起时有一些自定义的参数或者其他的数据

        # 下面这一段if处理表示的是调用方如果不传递某些参数，那么就用当前对象自己的属性
        if kwargs.get('method') == None:
            kwargs['method'] = self.method
        if kwargs.get('url') == None:
            kwargs['url'] = self.url
        if kwargs.get('params') == None:
            kwargs['params'] = self.params
        if kwargs.get('data') == None:
            kwargs['data'] = self.data
        if kwargs.get('json') == None:
            kwargs['json'] = self.json
        if kwargs.get('headers') == None:
            kwargs['headers'] = self.headers

        self.resp = self.client.send(**kwargs)
        return self.resp
    # 对于每一个接口来说，都有可能需要提取响应中的某个字段的值
    def get_resp(self,jsonpath_express):
        return jsonpath.jsonpath(self.resp.json(), jsonpath_express)[0]
    # 获取匹配到的所有的值
    def get_resp_all(self,jsonpath_express):
        return jsonpath.jsonpath(self.resp.json(), jsonpath_express)

