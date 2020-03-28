import unittest
from BeautifulReport import BeautifulReport
import time
from config.path import *
import os


def beautiful_runner(file_name, file_path, suite_key):  # file_path为cases\xxx
    _time = time.strftime("%Y-%m-%d %H_%M_%S")  # 格式化时间
    filename = "MRYX_report_{}_{}.html".format(file_name, _time)  # 以项目名+时间
    # 测试集
    file_path = os.path.join(PROJECT_PATH, file_path)  # 组装路径
    discover = unittest.defaultTestLoader.discover(file_path, pattern=suite_key)

    # 组装路径
    report_path = os.path.join(PROJECT_PATH, "report")
    BeautifulReport(discover).report(description="MRYX_张秋婷",
                                     report_dir=report_path,
                                     filename=filename)
