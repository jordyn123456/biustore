'''
@author: zhangqiuting
@software: Appium
@file: path.py
@time: 2020/3/26 11:04
@desc:
'''
from pathlib import Path


PROJECT_PATH = Path(__file__).absolute().parent.parent

LOG_PATH = PROJECT_PATH.joinpath("log")
