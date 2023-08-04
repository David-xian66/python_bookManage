# coding=utf-8
import json
import os
import io
import base64
from PIL import Image

from app.utils.log import Log as print
from app.utils.all_time import return_Time as NowTime
from app.utils.file import FileWrite


async def CheakAndSaveImg_ReturnPath(baseData, path, id):
    if baseData == None:
        return None
    else:
        img_base64 = baseData
        print(img_base64)
        # img_byte = base64.b64decode(img_base64.decode())
        img_byte = img_base64
        img_io = io.BytesIO(img_byte)
        img = Image.open(img_io)
        
        kind = str(img.format).lower()
        fileName = str(NowTime()) + '.' + str(kind)
        path = os.path.join(path, fileName)
        print.INFO(path)
        
        await FileWrite(baseData, path, 'wb')
        webPath = '/bookImg/' + id + '/' + fileName
        return webPath