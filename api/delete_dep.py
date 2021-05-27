# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/26 15:13
# @Copyright：北京码同学网络科技有限公司
from api.base_api import BaseApi


class DeleteDep(BaseApi):

    def __init__(self):
        #先实现父类的初始化函数
        BaseApi.__init__(self)
        self.url = self.host+'/cgi-bin/department/delete'
        self.method = 'get'
        # params参数存放要认证的token字段，那么他的值是动态变化的，在BaseApi中设计一个类属性token
        self.params = {
            'access_token': BaseApi.token,
            'id': 2
        }
