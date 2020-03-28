'''
@author: zhangqiuting
@software: SeleniumTest
@file: suite.py
@time: 2020/3/20 9:01
@desc:测试套件
'''

from runner.beautiful_runner import beautiful_runner

beautiful_runner("'我的'模块", r"cases", "MRYX_APP_WD_00*.py")


