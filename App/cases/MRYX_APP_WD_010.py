'''
@author: zhangqiuting
@software: Appium
@file: MRYX_APP_WD_001.py
@time: 2020/3/25 14:01
@desc:验证已登录状态，点击“我的”页面铃铛图标，进入消息页面功能
'''
from activities.splash_activity import *
from activities.main_activity import MainActivity
from time import sleep
import unittest
from common.logger import Logger
from activities.login_activity import LoginActivity
logger = Logger().logger


class WD(unittest.TestCase):
    def test_WD_001(self):
        # 实例化首页
        sa = SplashActivity()
        sleep(3)
        # 点击“我的”
        sa.find_element_xpath(sa.mine_path).click()
        sleep(2)
        # 实例化“我的”页面
        ma = MainActivity()
        ma.find_element_uiautomator_text("登录/注册").click()
        sleep(2)
        la = LoginActivity()
        la.find_element_uiautomator_text("请输入您的手机号").send_keys("13466666666")
        sleep(2)
        la.driver.find_element_by_id('cn.missfresh.application:id/iv_protocol').click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
