'''
@author: zhangqiuting
@software: Appium
@file: MRYX_APP_WD_008.py
@time: 2020/3/25 14:01
@desc:验证点击会员任务红包，进入会员专属任务页面功能
'''
from activities.splash_activity import *
from activities.main_activity import MainActivity
from time import sleep
import unittest
from activities.integral_activity import IntegralActivity
from activities.miss_fresh_event_activity import MissFreshEventActivity


class WD(unittest.TestCase):
    def test_WD_008(self):
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
        sleep(6)
        # 实例化积分兑换页面
        ia = IntegralActivity()
        # 点击“会员任务红包”
        ia.find_element_contains("会员任务红包").click()
        # 实例化会员专属页面
        mfea = MissFreshEventActivity()
        sleep(2)
        #TODO
        # mfea.find_element_contains("升级会员").click()
        # sleep(2)


if __name__ == '__main__':
    unittest.main()
