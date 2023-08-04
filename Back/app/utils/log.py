# coding=utf-8
"""日志系统"""
import datetime
import os.path
import sys
from typing import Any, Dict

# 日志系统 这个列表是暂存的 主窗口会定时 获取 -> 写入 -> 清空 (全局变量)
r = []


class Print_Colour:
    """
        HEADER:偏粉的紫色
        OKBLUE:蓝色
        OKCYAN:青色
        OKGREEN:绿色
        OKGREEN_2:有下划线的绿色
        WARNING:黄色
        WARNING_2:有下划线的黄色
        FAIL:红色
        FAIL_2:加粗的红色
        FAIL_3:有下划线的红色
        ENDC:正常的黑色
        BOLD:加粗的黑色
        UNDERLINE:有下横线的黑色
        GRAY:灰色
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[32m'
    OKGREEN_2 = '\033[4;32m'
    WARNING = '\033[93m'
    WARNING_2 = '\033[4;93m'
    FAIL = '\033[91m'
    FAIL_2 = '\033[1;91m'
    FAIL_3 = '\033[4;91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[37m'


class Log:
    def __init__(self, APP):
        """
            Log系统
            :param APP: 发送命令的系统
        """
        super(Log, self).__init__()
        self.APP = APP

    @staticmethod
    def INFO(P):
        P = str(P)
        Time_ = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
        # Time = Print_Colour.OKBLUE + '[' + Time_ + ']' + Print_Colour.ENDC + ' '
        Time = '[' + Time_ + ']' + ' '
        I = '[' + 'INFO' + '] '
        P_ = P
        # APP = '[' + Print_Colour.WARNING + self.APP + Print_Colour.ENDC + ']' + ' '
        APP = ''
        print(Time + APP + I + P_)
        # r.append(Time_ + ' ' + 'INFO ' + P)

    @staticmethod
    def DEBUG(P):
        P = str(P)
        Time_ = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
        # Time = Print_Colour.OKBLUE + '[' + Time_ + ']' + Print_Colour.ENDC + ' '
        Time = '[' + Time_ + ']' + ' '
        I = '[' + Print_Colour.WARNING + 'DEBUG' + Print_Colour.ENDC + '] '
        P_ = Print_Colour.GRAY + P + Print_Colour.ENDC
        # APP = '[' + Print_Colour.WARNING + self.APP + Print_Colour.ENDC + ']' + ' '
        APP = ''
        print(Time + APP + I + P_)
        r.append(Time_ + ' ' + 'DEBUG ' + P)

    @staticmethod
    def ERROR(P):
        P = str(P)
        Time_ = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
        # Time = Print_Colour.OKBLUE + '[' + Time_ + ']' + Print_Colour.ENDC + ' '
        Time = '[' + Time_ + ']' + ' '
        I = '[' + Print_Colour.FAIL + 'ERROR' + Print_Colour.ENDC + '] '
        P_ = Print_Colour.GRAY + P + Print_Colour.ENDC
        # APP = '[' + Print_Colour.WARNING + self.APP + Print_Colour.ENDC + ']' + ' '
        APP = ''
        print(Time + APP + I + P_)
        r.append(Time_ + ' ' + 'ERROR ' + P)


def Log_Return():
    """获取日志"""
    global r
    return r


def Log_Clear():
    """清空日志"""
    global r
    r = []


def returnLogFile():
    Path = os.path.join('Logs', datetime.datetime.now().strftime('%Y%m%d'))
    return Path


Sanic_Log: Dict[str, Any] = dict(  # no cov
    version=1,
    disable_existing_loggers=False,
    filename=returnLogFile(),
    filemode='a',  # 日志写入模式
    loggers={
        "sanic.root": {"level": "INFO", "handlers": ["console"]},
        "sanic.error": {
            "level": "INFO",
            "handlers": ["error_console"],
            "propagate": True,
            "qualname": "sanic.error",
        },
        "sanic.access": {
            "level": "INFO",
            "handlers": ["access_console"],
            "propagate": True,
            "qualname": "sanic.access",
        },
        "sanic.server": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": True,
            "qualname": "sanic.server",
        },
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout,
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stderr,
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": sys.stdout,
        },
    },
    formatters={
        "generic": {
            "format": "%(asctime)s [%(levelname)s] %(message)s",
            "datefmt": "[%m/%d %H:%M:%S]",
            "class": "logging.Formatter",
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: "
                      + "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%m/%d %H:%M:%S]",
            "class": "logging.Formatter",
        },
    },
)

# if __name__ == '__main__':
#     r = []
#     Log.ERROR('1111')
#     Log.INFO('asdasdas')
#     Log.DEBUG('askdnasnnaksldnklas')
