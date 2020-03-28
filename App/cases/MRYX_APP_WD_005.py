'''
@author: zhangqiuting
@software: Appium
@file: MRYX_APP_WD_005.py
@time: 2020/3/25 14:01
@desc:验证点击积分兑换，进入积分兑换页面功能
'''
from activities.splash_activity import *
from activities.main_activity import MainActivity
from time import sleep
import unittest


class WD(unittest.TestCase):
    def test_WD_005(self):
        # 实例化首页
        sa = SplashActivity()
        sleep(3)
        # 点击“我的”
        sa.find_element_xpath(sa.mine_path).click()
        sleep(2)
        # 实例化“我的”页面
        ma = MainActivity()
        sleep(5)
        # 点击“积分兑换”
        ma.find_element_contains("积分兑换").click()
        # 断言，判断当前页面是否是所需页面
        current_focus = 'cn.missfresh.module.promotion.integral.view.IntegralActivity'
        self.assertEqual(current_focus, ma.driver.current_activity)


if __name__ == '__main__':
    unittest.main()
