# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/25 15:24
# @Copyright：北京码同学网络科技有限公司
import jsonpath
import requests

from api.base_api import BaseApi


class GetToken(BaseApi):

    def __init__(self):
        #先实现父类的初始化函数
        BaseApi.__init__(self)
        self.url = self.host+'/cgi-bin/gettoken'
        self.method = 'get'
        self.params = {
                'corpid': 'wwcbd4b282b8bd5daa',
                'corpsecret': '39M32nSCJwylrcsyCPS95AruULEaxi2A91v2qD4V-xM'
        }

if __name__ == '__main__':
    get_token = GetToken()
    print(get_token.send())
    print(get_token.get_resp('$.access_token'))


# url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
#
# params = {
#     'corpid': 'wwcbd4b282b8bd5daa',
#     'corpsecret': '39M32nSCJwylrcsyCPS95AruULEaxi2A91v2qD4V-xM'
# }
#
# #get方法中的参数就是接口的基本信息，url表示接口地址，params表示接口参数
# # resp表示接口发起之后得到的结果对象
# resp = requests.get(url=url,params=params)
# print(resp.text)# resp.text表示响应里的内容
# # print(resp)
#
# # 提取响应里的access_token
# print(jsonpath.jsonpath(resp.json(), '$.access_token')[0])
# requests.get #发起get
# requests.post #发起post
# requests.put #发起put
# requests.delete #发起delete

