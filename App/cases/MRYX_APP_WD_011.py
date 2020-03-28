'''
@author: zhangqiuting
@software: Appium
@file: MRYX_APP_WD_011.py
@time: 2020/3/25 14:01
@desc:验证清除缓存功能
'''
from activities.splash_activity import *
from activities.main_activity import MainActivity
from time import sleep
import unittest
from common.logger import Logger
from common import swipe
from activities.set_activity import SetActivity

logger = Logger().logger


class WD(unittest.TestCase):
    def test_WD_011(self):
        # 实例化首页
        sa = SplashActivty()
        sleep(3)
        # 点击“我的”
        sa.find_element_xpath(sa.mine_path).click()
        sleep(2)
        # 实例化“我的”页面
        ma = MainActivity()
        # 上滑现出设置
        swipe.swipeUp(ma.driver, 200)
        # 点击设置
        ma.find_element_uiautomator_text("设置").click()
        sleep(3)
        # 点击清除缓存
        ma.find_element_contains("清除缓存").click()
        # 断言
        sa = SetActivity()
        text = sa.catch_toast()
        self.assertIn("清除了", text)


if __name__ == '__main__':
    unittest.main()
