# coding=utf-8
import asyncio
import json
import shutil

import aiofiles


def system():
    """
        return: Mac Win Linux
        'win32':Windows
        'cygwin':Windows/Cygwin
        'darwin':macOS
        'aix':AIX
        'linux':Linux
    """
    from sys import platform
    a = str(platform)
    if a == 'win32' or a == 'cygwin':
        s = 'Win'
    elif a == 'darwin':
        s = 'Mac'
    elif a == 'linux' or a == 'aix':
        s = 'Linux'
    return s

def DeletePath(FilePath):
    """
        delete文件
        :param Data: 内容
        :param FilePath: 路径
        :param kind: 种类
    """
    shutil.rmtree(FilePath)
    return True




async def FileWrite(Data, FilePath, kind='w+'):
    """
        写入文件
        :param Data: 内容
        :param FilePath: 路径
        :param kind: 种类
    """
    if kind != 'wb':
        async with aiofiles.open(FilePath, kind, encoding='utf_8') as f:
            await f.write(Data)
            await f.close()
    else:
        async with aiofiles.open(FilePath, kind) as f:
            await f.write(Data)
            await f.close()
    return True

async def JsonWrite(Json_, JsonFile):
    """
        写入Json
        :param Json_: Json内容
        :param JsonFile: Json路径
    """
    async with aiofiles.open(JsonFile, 'w+', encoding='utf_8') as f:
        a = json.dumps(Json_, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
        await f.write(a)
        await f.close()
    return True


def JsonWrite_NotAsync(Json_, JsonFile):
    """
        写入Json
        :param Json_: Json内容
        :param JsonFile: Json路径
    """
    with open(JsonFile, 'w+', encoding='utf_8') as f:
        json.dump(Json_, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


async def JsonRead(JsonFile):
    """
        读取Json
        JsonFile = Json的目录
    """
    try:
        async with aiofiles.open(JsonFile, 'r', encoding='utf_8') as f:
            f_r = await f.read()
        return json.loads(f_r, strict=False)
    except json.decoder.JSONDecodeError:
        try:
            await asyncio.sleep(0.2)
            async with aiofiles.open(JsonFile, 'r', encoding='utf_8') as f:
                f_r = await f.read()
            return json.loads(f_r, strict=False)
        except json.decoder.JSONDecodeError:
            return None, "json.decoder.JSONDecodeError"


def JsonRead_NotAsync(JsonFile):
    """
        读取Json
        JsonFile = Json的目录
    """
    with open(JsonFile, 'r', encoding='utf_8') as f:
        # print(JsonFile)
        r = json.load(f, strict=False)
    return r
