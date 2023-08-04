# coding=utf-8
""" URL: /api/panel """
from sanic import Blueprint, json

from app.utils.api import OK_Json, return_lang, CheckRequestLogin, Error_Json
from app.utils.api import return_AllLanguage as AllLanguage
from app.utils.api import return_ErrorRequest as ErrorRequest
from app.utils.file import JsonWrite
from app.utils.log import Log as print

Json = JsonFile_Path = overview_JSON = None
Back_Users_Session = 'Back_Users_Session'

# 蓝图panel_bp,URL前缀'/api/panel'
notice_bp = Blueprint('notice', url_prefix='/api/index/notice')


# 在蓝图中定义一些路由
@notice_bp.route("list_api", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def root(request):
    """获取notice"""
    global Json
    print.INFO('* -> /api/index/notice/list_api')
    if request.method == 'GET':
        return json(OK_Json({}, "查询成功"), status=200)
    else:
        return json(body=ErrorRequest(), status=405)



def SetData(data, Back_Users_Session_):
    global Data, Json, JsonFile_Path, overview_JSON, Back_Users_Session, BooksJsonFile_Path, BooksJson
    Data = data
    Json = Data.Json
    JsonFile_Path = Data.JsonFile_Path
    overview_JSON = Data.overview_JSON
    Back_Users_Session = Back_Users_Session_
    BooksJsonFile_Path = Data.BooksJsonFile_Path
    BooksJson = Data.BooksJson

