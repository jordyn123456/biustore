'''
@author: zhangqiuting
@software: Appium
@file: my_balance_activity.py
@time: 2020/3/25 23:19
@desc:
'''
from activities.splash_activity import SplashActivity

class MyBalanceActivity(SplashActivity):
    '''我的余额页面'''
    # 定位【立即充值】按钮
    charge_button_path = '//android.widget.Button[@resource-id=\"cn.missfresh.application:id/btn_recharge\"]'
