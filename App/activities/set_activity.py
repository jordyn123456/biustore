'''
@author: zhangqiuting
@software: Appium
@file: set_activity.py
@time: 2020/3/27 8:53
@desc:
'''
from activities.splash_activity import SplashActivity
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support import expected_conditions as EC


class SetActivity(SplashActivity):
    '''
    设置页面
    '''
    toast_locator = (By.XPATH, "//*[contains(@text,'清除了')]")

    def catch_toast(self):
        wait = WebDriverWait(self.driver, 5, 0.3)  # 实例化显式等待
        wait.until(EC.presence_of_element_located(self.toast_locator))  # 表示直到toast出现
        toast = self.driver.find_element(*self.toast_locator).text
        return toast