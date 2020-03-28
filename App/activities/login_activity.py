'''
@author: zhangqiuting
@software: Appium
@file: login_activity.py
@time: 2020/3/26 16:44
@desc:
'''
from activities.splash_activity import SplashActivity

class LoginActivity(SplashActivity):
    '''
    登录页面
    '''
    # 定位勾选框
    check_box_path = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.ImageView[2]'