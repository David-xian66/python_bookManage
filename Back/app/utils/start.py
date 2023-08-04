# coding=utf-8
import json
import os
from app.utils.log import Log as print
from app.utils.file import JsonRead_NotAsync, JsonWrite_NotAsync


def CheckJson(JsonFile_Path, Json):
    if not os.path.isfile(JsonFile_Path) or not os.path.getsize(JsonFile_Path):
        print.INFO(str(JsonFile_Path) + '文件缺少,正在补全…')
        JsonWrite_NotAsync(Json, JsonFile_Path)
        print.INFO(str(JsonFile_Path) + '文件以补全')
    else:
        try:
            print.INFO(str(JsonFile_Path) + ' Json检查开始')
            j_f = JsonRead_NotAsync(JsonFile_Path)
            C = 0
            for J_C_1 in Json:
                if J_C_1 not in j_f:
                    j_f[J_C_1] = Json[J_C_1]
                    C = 1
                elif type(Json[J_C_1]) == dict:
                    for J_C_1_1 in Json[J_C_1]:
                        # print.INFO(J_C_1_1)
                        # print.INFO(J_C_1)
                        if J_C_1_1 not in j_f[J_C_1]:
                            j_f[J_C_1][J_C_1_1] = Json[J_C_1][J_C_1_1]
                            C = 1

            if C == 1:
                print.INFO(str(JsonFile_Path) + '文件缺少,正在补全…')
                JsonWrite_NotAsync(j_f, JsonFile_Path)
                print.INFO(str(JsonFile_Path) + '文件以补全')
            else:
                print.INFO(str(JsonFile_Path) + '文件完整')

        except json.decoder.JSONDecodeError:
            print.ERROR('Json配置文件损坏,请修复或删除文件配置文件并重启(会自动为您生成新配置文件)')
            exit(-1)



def Check_Config(print):
    print.INFO('开始检查config.json')
    Json = {
        'Back_IPPort': {
            'IP': '0.0.0.0',
            'Port': 9001
        },
        'Debug': True,
        'Back_Users': {},
        'Front_Users': {},
        'Back_Users_Session': {},
        'Front_Users_Session': {},
        # 'lang': 'en_US'
    }
    Json2 = {
        'Tag':[],
        'Class':[],
        'BookID':0,
        'ClassID':0,
        'TagID':0,
    }
    JsonFile_Path = os.path.join('config.json')
    CheckJson(JsonFile_Path,Json)
    JsonFile_Path = os.path.join('Books','config.json')
    CheckJson(JsonFile_Path,Json2)


def return_BackIPAndPort():
    """
        返回后端在配置文件中的IP和Port
        :return [IP,Port]
    """
    file_path = os.path.join('config.json')
    J = JsonRead_NotAsync(file_path)
    return [J['Back_IPPort']['IP'], J['Back_IPPort']['Port']]
