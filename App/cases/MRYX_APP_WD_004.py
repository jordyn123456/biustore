'''
@author: zhangqiuting
@software: Appium
@file: MRYX_APP_WD_004.py
@time: 2020/3/25 14:01
@desc:验证点击充值说明，弹出说明弹框功能
'''
from activities.splash_activity import *
from activities.main_activity import MainActivity
from activities.my_balance_activity import MyBalanceActivity
from activities.recharge_activity import RechargeActivity
from time import sleep
from common.swipe import swipeLeft
import unittest


class WD(unittest.TestCase):
    def test_WD_004(self):
        # 实例化首页

        sa = SplashActivity()
        sleep(3)
        # 点击“我的”
        sa.find_element_xpath(sa.mine_path).click()
        sleep(2)
        # 实例化“我的”页面
        ma = MainActivity()
        sleep(2)
        # 点击“余额”
        ma.find_element_xpath(ma.charge_path).click()
        # 实例化我的余额页面
        mba = MyBalanceActivity()
        # 点击“立即充值按钮”
        sleep(2)
        mba.find_element_xpath(mba.charge_button_path).click()
        # 实例化余额充值页面
        ra = RechargeActivity()
        sleep(2)
        ra.find_element_uiautomator_text("充值说明").click()
        # ra.find_element_contains("充值说明").click()
        # 断言，在弹框中找到“余额说明”
        sleep(3)
        text = ra.find_element_xpath(ra.recharge_bouncing_frame).find_element_by_android_uiautomator('new UiSelector().text("余额说明")').get_attribute('text')
        self.assertEqual(text, "余额说明")

if __name__ == '__main__':
    unittest.main()
