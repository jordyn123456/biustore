'''
@author: zhangqiuting
@software: Appium
@file: miss_fresh_event_activity.py
@time: 2020/3/26 13:59
@desc:
'''
from activities.splash_activity import SplashActivity
import time


class MissFreshEventActivity(SplashActivity):
    '''
    会员专属任务页面
    '''

    def get_month(self):
        now_month = int(time.strftime("%m"))
        month_list = []
        for i in range(1, 6):
            if now_month - i > 0:
                month_list.append("0" + str(now_month - i))
            else:
                month_list.append(str(now_month - i + 12))
        return month_list


# a = MissFreshEventActivity()
# print(a.get_month())