# coding=utf-8

def return_AllAlphabet():
    """return 所有字母(小写)"""
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def return_AllMajuscule():
    """return 所有大写字母"""
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def return_AllNumber(str_=True):
    """
        return 所有大写字母
        :param str_ : 是否用字符串返回
    """
    if str_:
        return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    else:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
