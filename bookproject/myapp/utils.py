import hashlib


def md5value(key):
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    md5str = (input_name.hexdigest()).lower()
    print('计算md5:', md5str)
    return md5str
