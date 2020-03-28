'''
@author: zhangqiuting
@software: Appium
@file: swipe.py
@time: 2020/3/24 22:28
@desc:页面滑动方法
'''


# 获得机器屏幕大小x,y
def getSize(dr):
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)  # (720,1280)


# 屏幕向上滑动
def swipeUp(dr, t):
    l = getSize(dr)  # (720,1280)
    x1 = int(l[0] * 0.5)  # x坐标  360
    y1 = int(l[1] * 0.75)  # 起始y坐标  960
    y2 = int(l[1] * 0.25)  # 终点y坐标  320
    dr.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipeDown(dr, t):
    l = getSize(dr)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    dr.swipe(x1, y1, x1, y2, t)


# 屏幕向左滑动,y为竖向所占窗口比例
def swipeLeft(dr, t, y):
    l = getSize(dr)
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * y)
    x2 = int(l[0] * 0.05)
    dr.swipe(x1, y1, x2, y1, t)


# 屏幕向右滑动
def swipeRight(dr, t):
    l = getSize(dr)
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    dr.swipe(x1, y1, x2, y1, t)


# 屏幕快速向右滑动
def flickSwipeRight(dr):
    l = getSize(dr)
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    dr.flick(x1, y1, x2, y1)


from appium.webdriver.common.touch_action import TouchAction


# 9宫格解锁方法，需要传第一个点的坐标、点间距、解锁点位顺序lst
def unlock(driver, x, y, interval, lst):
    action = TouchAction(driver)  # 实例化触摸类
    dct_grid = {}
    flag = True  # 定flag简化流程
    count = 0
    for i in range(9):
        dct_grid[i + 1] = (x, y)  # 给1-9添加对应坐标
        x = x + interval
        count = count + 1
        if count == 3:
            count = 0
            y = y + interval
            x = x - 3 * interval

    for i in lst:  # 取出点位顺序
        x, y = dct_grid.get(i)  # 点位赋值给x、y
        if flag == True:
            action.press(x=x, y=y)  # 主意x=和y=，不要忘了=，这里是按下不提起
            flag = False
        action.move_to(x=x, y=y)  # 移动
        action.wait(300)
    action.release()  # 提起
    action.perform()  # 提交动作
