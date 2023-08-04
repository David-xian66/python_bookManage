# coding=utf-8
import hashlib
import hmac
import random


from app.utils.all_time import return_Time


def NewUUID():
    """生成UUID"""
    uuid = hmac.new(str(return_Time(True)).encode(), str(return_Time()).encode(), hashlib.sha1).hexdigest()
    for a in range(1, 2):
        b = str(random.uniform(1.0001, 100000000000.0001))
        uuid += hmac.new(str(b).encode(), str(return_Time()).encode(), hashlib.sha1).hexdigest()
    return uuid


def HMAC_New(Text_, Key):
    """HMAC加密"""
    return hmac.new(Text_.encode(), Key.encode(), hashlib.sha1).hexdigest()


def NewMD5(text):
    """MD5加密"""
    return hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()
