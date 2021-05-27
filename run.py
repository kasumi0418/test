# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/5/25 15:12
# @Copyright：北京码同学网络科技有限公司
import os

import pytest

if __name__ == '__main__':
    pytest.main()
    #想自动生成报告，那么还需要安装allure的命令行工具
    os.system('allure generate ./report/wx -o ./report/html --clean')
