'''
@author: zhangqiuting
@software: Appium
@file: MRYX_APP_WD_007.py
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
    def test_WD_007(self):
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
        # 实例化会员专属任务页面
        mfea = MissFreshEventActivity()
        sleep(5)
        #TODO
        # mfea.find_element_xpath('//android.view.View[@resource-id=\"historyWrap21\"]').click()
        # mfea.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("historyWrap00")').click()
        # print(text)
        # for i in range(5):
        #     swipe.swipeUp(mfea.driver, 500)
        #     sleep(2)
        #     month_text = mfea.get_month()[i]
            # text = mfea.find_element_uiautomator_text("12月").get_attribute("text")
            # print(text)
            # mfea.find_element_uiautomator_text("{}月".format(month_text)).click()
            # sleep(5)


if __name__ == '__main__':
    unittest.main()
