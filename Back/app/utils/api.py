# coding=utf-8
import os

from app.utils.all_time import return_Time
from app.utils.file import JsonRead
from app.utils.strind_data import return_AllNumber, return_AllMajuscule, return_AllAlphabet


def return_ErrorRequest():
    """返回默认的错误请求Json"""
    J = {
        "status": 0,
        "data": "string",
        "time": return_Time()
    }
    return J


async def return_AllLanguage():
    """返回所有语言"""
    J = await JsonRead(os.path.join('langs', 'langs.json'))
    AllLanguage = J['list']
    return AllLanguage


def passwordCheck(password):
    """
        检查密码是否合规(8-15个字符',至少1个大写字母',1个小写字母',1个数字',不能有特殊符号)
        :return True or False
    """
    password = list(password)
    password_l = len(password)
    if 8 <= password_l <= 15:
        BigL = 0
        SmallL = 0
        N = 0
        All_S = return_AllAlphabet()  # 小写字母列表
        All_B = return_AllMajuscule()  # 大写字母列表
        All_N = return_AllNumber()  # 数字列表
        for p in password:
            if p in All_S:
                SmallL += 1
            elif p in All_B:
                BigL += 1
            elif p in All_N:
                N += 1
            else:
                # 含有特殊字符
                return False
        if BigL >= 1 and SmallL >= 1 and N >= 1:
            return True
        else:
            return False
    else:
        return False


async def return_lang(Json):
    """
        return 面板当前语言数据
        :param Json: 面板json配置
    """
    l = Json['lang']
    r_list = []
    Json_AllLang = await JsonRead(os.path.join('langs', 'langs.json'))
    Json_AllLang_1 = Json_AllLang['langs']
    r_list.append(Json_AllLang_1[l])
    for a in Json_AllLang_1:
        if a != l:
            r_list.append(Json_AllLang_1[a])

    r_Json = {
        'langs': r_list,
        'json': {}
    }

    l_json = await JsonRead(os.path.join('langs', l + '.json'))
    l_json = l_json['front']
    for a in l_json:
        r_Json['json'][a] = l_json[a]

    return r_Json


def CheckRequestLogin(request, Json):
    """检查请求是否登陆"""
    if request.ctx.session.sid in Json:
        return True
    else:
        return False


def OK_Json(data, msg=None, code=200):
    """请求模板(传递data,msg,code值,返回完整的返回Json)"""
    return {
        "code": code,
        "data": data,
        "msg": msg,
        "time": return_Time()
    }
    
def NoOK_Json(msg=None, code=200):
    """请求模板(传递data,msg,code值,返回完整的返回Json)"""
    return {
        "code": code,
        "msg": msg,
        "time": return_Time()
    }

def Error_Json(code, data, error):
    """请求模板(传递code:http状态码 data:数据 和 error:错误信息,返回完整json)"""
    return {
        "status": code,
        "error": error,
        "data": data,
        "time": return_Time()
    }


def return_VisitData():
    return [
            {
                "day": "2023-06-30",
                "uv": 25,
                "pv": 192
            },
            {
                "day": "2023-07-01",
                "uv": 21,
                "pv": 160
            },
            {
                "day": "2023-07-02",
                "uv": 38,
                "pv": 279
            },
            {
                "day": "2023-07-03",
                "uv": 24,
                "pv": 186
            },
            {
                "day": "2023-07-04",
                "uv": 29,
                "pv": 127
            },
            {
                "day": "2023-07-05",
                "uv": 21,
                "pv": 195
            },
            {
                "day": "2023-07-06",
                "uv": 23,
                "pv": 125
            }
    ]
    

def return_ClassificationRankData():
    return [
        {
            "title": "文学",
            "count": 61
        },
        {
            "title": "娱乐",
            "count": 40
        },
        {
            "title": "财经",
            "count": 31
        },
        {
            "title": "历史",
            "count": 29
        },
        {
            "title": "生活",
            "count": 29
        }
    ]


def return_BorrowRankData():
    return [
        {
            "book_id": 305,
            "title": "无感之谜",
            "count": 24
        },
        {
            "book_id": 304,
            "title": "测试图书209",
            "count": 9
        },
        {
            "book_id": 302,
            "title": "生活图书28",
            "count": 4
        },
        {
            "book_id": 257,
            "title": "历史图书13",
            "count": 3
        },
        {
            "book_id": 256,
            "title": "历史图书12",
            "count": 2
        },
        {
            "book_id": 303,
            "title": "生活图书29",
            "count": 2
        },
        {
            "book_id": 299,
            "title": "生活图书25",
            "count": 2
        },
        {
            "book_id": 32,
            "title": "测试图书8",
            "count": 1
        },
        {
            "book_id": 113,
            "title": "经济图书19",
            "count": 1
        },
        {
            "book_id": 251,
            "title": "历史图书7",
            "count": 1
        },
        {
            "book_id": 268,
            "title": "历史图书24",
            "count": 1
        },
        {
            "book_id": 294,
            "title": "生活图书20",
            "count": 1
        },
        {
            "book_id": 53,
            "title": "测试图书19",
            "count": 1
        },
        {
            "book_id": 206,
            "title": "管理图书22",
            "count": 1
        },
        {
            "book_id": 271,
            "title": "历史图书27",
            "count": 1
        },
        {
            "book_id": 298,
            "title": "生活图书24",
            "count": 1
        },
        {
            "book_id": 74,
            "title": "测试图书10",
            "count": 1
        },
        {
            "book_id": 222,
            "title": "互联网图书8",
            "count": 1
        },
        {
            "book_id": 281,
            "title": "生活图书7",
            "count": 1
        },
        {
            "book_id": 25,
            "title": "测试图书1",
            "count": 1
        },
        {
            "book_id": 85,
            "title": "测试图书21",
            "count": 1
        },
        {
            "book_id": 241,
            "title": "互联网图书27",
            "count": 1
        },
        {
            "book_id": 261,
            "title": "历史图书17",
            "count": 1
        },
        {
            "book_id": 292,
            "title": "生活图书18",
            "count": 1
        },
        {
            "book_id": 301,
            "title": "生活图书27",
            "count": 1
        }
    ]


def AddAllClassInClassData(ClassData):
    A = list(ClassData)
    A.insert(0, {
        "key": -1,
        "title": "全部",
        "isParent": True,
        "children": []
    })
    return A