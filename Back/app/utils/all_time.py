# coding=utf-8
import datetime
import time


def return_Time(Point=False):
    """
        返回当前时间
        :param Point: 是否带小数点
    """
    if not Point:
        time_ = str(time.time()).split('.')[0]
    else:
        time_ = time.time()
    return time_


def return_DateAndTime():
    """返回日前和时间"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
