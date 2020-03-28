'''
@author: zhangqiuting
@software: Appium
@file: MRYX_APP_WD_003.py
@time: 2020/3/25 14:01
@desc:验证切换重置金额功能
'''
from activities.splash_activity import *
from activities.main_activity import MainActivity
from activities.my_balance_activity import MyBalanceActivity
from activities.recharge_activity import RechargeActivity
from time import sleep
from common.swipe import swipeLeft
import unittest


class WD(unittest.TestCase):
    def test_WD_003(self):
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
        mba.find_element_xpath(mba.charge_button_path).click()
        sleep(2)
        # 实例化余额充值页面
        ra = RechargeActivity()
        # 点击第一个金额
        ra.find_element_xpath(ra.money_first_path).click()
        sleep(2)
        # 断言其对应充值卡的文本与其文本一致
        text_first_1 = ra.find_element_xpath(ra.money_first_path).text
        text_first_2 = ra.find_element_xpath(ra.money_text_path).text
        self.assertEqual(text_first_1, text_first_2)
        # 滑动金额卡，切换至最后一个金额卡
        swipeLeft(ra.driver, 500, 0.2)
        sleep(1)
        swipeLeft(ra.driver, 500, 0.2)
        sleep(1)
        swipeLeft(ra.driver, 500, 0.2)
        # 断言其对应充值卡的文本与最后一个金额文本一致
        text_last_1 = ra.find_element_xpath(ra.money_last_path).text
        text_last_2 = ra.find_element_xpath(ra.money_text_path).text
        self.assertEqual(text_last_1, text_last_2)


if __name__ == '__main__':
    unittest.main()
