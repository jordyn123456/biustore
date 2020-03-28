'''
@author: zhangqiuting
@software: Appium
@file: base_page.py
@time: 2020/3/25 14:49
@desc:
'''
from appium import webdriver
from appium.webdriver.common.mobileby import By


class SplashActivity():
    '''
    首页，作为基础页面，包含配置信息、driver以及首页元素、xpath定位方法封装
    '''
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '5.1.1',
        'appPackage': 'cn.missfresh.application',
        'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
        'noReset': True,
        'automatorName': 'Uiautomator2',
        'newCommandTimeout': 600
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    # “我的”定位
    mine_path = '//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/cv_main_bottom_tab_layout\"]/android.widget.FrameLayout[5]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]'

    def find_element_xpath(self, path):
        return self.driver.find_element(By.XPATH, path)

    def find_element_uiautomator_text(self, text):
        return self.driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(text))

    def find_element_contains(self, text):
        return self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("{}")'.format(text))

