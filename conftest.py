# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/25 15:11
# @Copyright：北京码同学网络科技有限公司
import pytest

from api.base_api import BaseApi
from api.delete_dep import DeleteDep
from api.get_dep import GetDep
from api.get_token import GetToken


@pytest.fixture(scope='session',autouse=True)
def get_token():
    get_token = GetToken()
    get_token.send()
    BaseApi.token = get_token.get_resp('$.access_token')

@pytest.fixture(scope='class')
def delete_dep_data():
    # 调用接口删除数据，问题是删除接口需要部门id，id从何而来？
    # 可以调用获取部门的接口得到所有的部门id值
    get_dep = GetDep()
    get_dep.send()
    id_list  = get_dep.get_resp_all('$..id')
    delete_dep = DeleteDep()
    #遍历获取到的所有的id，一一进行删除
    for i in id_list:
        delete_dep.params['id'] = i
        delete_dep.send()


