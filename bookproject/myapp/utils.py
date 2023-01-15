import hashlib


def md5value(key):
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    md5str = (input_name.hexdigest()).lower()
    print('计算md5:', md5str)
    return md5str


def dict_fetchall(cursor):  # cursor是执行sql_str后的记录，作入参
    columns = [col[0] for col in cursor.description]  # 得到域的名字col[0]，组成List
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def get_ip(request):
    """
    获取请求者的IP信息
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
