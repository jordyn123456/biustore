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
        # 点击铃铛图标
        ma.find_element_xpath(ma.bell_path).click()
        # 断言，判断当前页面是否是所需页面
        current_focus = 'cn.missfresh.module.user.mine.view.MsgListActivity'
        logger.info(ma.driver.current_activity)
        self.assertEqual(current_focus, ma.driver.current_activity)


if __name__ == '__main__':
    unittest.main()
