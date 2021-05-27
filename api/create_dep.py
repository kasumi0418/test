# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/26 15:06
# @Copyright：北京码同学网络科技有限公司
from api.base_api import BaseApi
from api.get_token import GetToken


class CreateDep(BaseApi):

    def __init__(self):
        #先实现父类的初始化函数
        BaseApi.__init__(self)
        self.url = self.host+'/cgi-bin/department/create'
        self.method = 'post'
        # params参数存放要认证的token字段，那么他的值是动态变化的，在BaseApi中设计一个类属性token
        self.params = {
            'access_token': BaseApi.token
        }
        # 在这里给json赋值，表示的是单接口的默认参数
        self.json = {
           "name": "默认部门",
           "name_en": "RDGZ16",
           "parentid": 1,
           "order": 1,
           "id": 2
        }
if __name__ == '__main__':
    get_token = GetToken()
    print(get_token.send())
    BaseApi.token = get_token.get_resp('$.access_token')
    create_dep = CreateDep()
    print(create_dep.send().text)

