# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/26 15:17
# @Copyright：北京码同学网络科技有限公司
import allure
import pytest

from api.base_api import BaseApi
from api.create_dep import CreateDep
from api.get_token import GetToken


class TestCretaeDep:



    """
    部门添加正确,{"name":"教学部","name_en":"RDGZ","parentid":1,"order":1,"id":2}
    部门添加正确-只有必填项,{"name":"python教学部","parentid":1}
    部门名称重复,{"name":"教学部","name_en":"RDGZ1","parentid":1,"order":1,"id":3}
    部门英文名称重复,{"name":"教学部1","name_en":"RDGZ","parentid":1,"order":1,"id":4}
    父级部门不存在,{"name":"教学部2","name_en":"RDGZ2","parentid":1000,"order":1,"id":5}
    部门id重复,{"name":"教学部3","name_en":"RDGZ3","parentid":1,"order":1,"id":2}
    """
    """
    当前写法存在的问题
    1. 数据问题，每次请求前没有清除原有数据，造成数据异常
       清除原有数据的方案：
       1. 直接操作数据库干掉原有数据(做的企业微信，没有库权限)
       2. 调用接口删除原有数据(作为一个pytest的fixture进行实现)
    2. 每一个测试用例都获取了token，不方便，如何优化
       采用pytest的fixture来实现token的获取
    """

    tests_data= [
        ['部门添加正确-只有必填项',{"name":"python教学部","parentid":1},0],
        ['部门添加正确',{"name":"教学部","name_en":"RDGZ","parentid":1,"order":1,"id":3},0],
        ['部门名称重复',{"name":"教学部","name_en":"RDGZ1","parentid":1,"order":1,"id":4},60008],
        ['部门英文名称重复',{"name":"教学部1","name_en":"RDGZ","parentid":1,"order":1,"id":5},60008],
        ['父级部门不存在',{"name":"教学部2","name_en":"RDGZ2","parentid":1000,"order":1,"id":6},60004],
        ['部门id重复',{"name":"教学部3","name_en":"RDGZ3","parentid":1,"order":1,"id":2},60008]
    ]
    #调用pytest的装饰器，在装饰器里写上测试数据每一列对应的变量名称,然后再写上测试数据列表
    #并且在测试用例方法参数中增加对应的参数名称
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,json,assertvalue',tests_data)
    def test_cretae_dep(self,casename,json,assertvalue,delete_dep_data):
        create_dep = CreateDep()
        create_dep.send(json=json) #原来是只发起默认的参数，现在要根据传进来的测试数据发起不同的参数
        # 断言
        #提取响应里的errcode来作为判断依据
        errcode = create_dep.get_resp('$.errcode')
        assert errcode == assertvalue #原来是断言的默认参数值，现在要根据传进来的测试数据断言不同的值
    # def test_cretae_dep1(self,delete_dep_data):
    #     create_dep = CreateDep()
    #     create_dep.send()
    #     # 断言
    #     #提取响应里的errcode来作为判断依据
    #     errcode = create_dep.get_resp('$.errcode')
    #     assert errcode == 0
    # def test_cretae_dep2(self,delete_dep_data):
    #     create_dep = CreateDep()
    #     create_dep.send()
    #     # 断言
    #     #提取响应里的errcode来作为判断依据
    #     errcode = create_dep.get_resp('$.errcode')
    #     assert errcode == 0