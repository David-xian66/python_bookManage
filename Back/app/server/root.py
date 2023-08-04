# coding=utf-8
""" URL: /(HTML) """
from sanic import Blueprint, json
# from app.settings import Json, JsonFile_Path
from app.utils.algorithm_data import NewUUID, HMAC_New, NewMD5
from app.utils.all_time import return_DateAndTime as NowDateTime
from app.utils.all_time import return_Time as NowTime
from app.utils.api import passwordCheck
from app.utils.api import return_ErrorRequest as ErrorRequest, CheckRequestLogin, OK_Json
from app.utils.file import JsonWrite
from app.utils.log import Log as print
from sanic.response import file
import os

Json = JsonFile_Path = overview_JSON = None
Back_Users_Session = 'Back_Users_Session'

root_bp = Blueprint('root', url_prefix='/')


# 在蓝图中定义一些路由

root_bp.static("/", os.path.join(".","dist","index.html"))
root_bp.static("/legacy-assets-index.html.json", os.path.join(".","dist","legacy-assets-index.html.json"))
root_bp.static("/css/", os.path.join(".","dist","css"))
root_bp.static("/img/", os.path.join(".","dist","img"))
root_bp.static("/js/", os.path.join(".","dist","js"))



# 图书照片
@root_bp.route("/bookImg/<bookid>/<imgame>")
async def handler(request, bookid, imgame):
    path = os.path.join('Books', bookid, imgame)
    return await file(path)



def SetData(data, Back_Users_Session_):
    global Data, Json, JsonFile_Path, overview_JSON, Back_Users_Session
    Data = data
    Json = Data.Json
    JsonFile_Path = Data.JsonFile_Path
    overview_JSON = Data.overview_JSON
    Back_Users_Session = Back_Users_Session_
