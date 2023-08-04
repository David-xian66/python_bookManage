# coding=utf-8
""" URL: /api/panel """
from sanic import Blueprint, json

from app.utils.api import OK_Json, return_lang, CheckRequestLogin, Error_Json, return_ClassificationRankData, return_VisitData, return_BorrowRankData
from app.utils.api import return_AllLanguage as AllLanguage
from app.utils.api import return_ErrorRequest as ErrorRequest
from app.utils.file import JsonWrite
from app.utils.log import Log as print

Json = 'Data.Json'
JsonFile_Path = 'Data.JsonFile_Path'
overview_JSON = 'Data.overview_JSON'
Back_Users_Session = 'Back_Users_Session'
BooksJsonFile_Path = 'BooksJsonFile_Path'
BooksJson = 'BooksJson'

# 蓝图panel_bp,URL前缀'/api/panel'
overview_bp = Blueprint('overview', url_prefix='/api/admin/overview/')


# 在蓝图中定义一些路由
@overview_bp.route("/count", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def root(request):
    """获取list"""
    global Json, BooksJson
    print.INFO('* -> /api/admin/overview/count')
    if request.method == 'GET':
        print.INFO(BooksJson)
        data = {
            "book_count": 280,
            "book_week_count": 0,
            "borrow_count": 41,
            "borrow_person_count": 25,
            "return_count": 23,
            "return_person_count": 16,
            "overdue_count": 42,
            "overdue_person_count": 14,
            "borrow_rank_data": return_BorrowRankData(),
            "classification_rank_data": return_ClassificationRankData(),
            "visit_data": return_VisitData()
        }
        return json(OK_Json(data, '查询成功'), status=200)
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

