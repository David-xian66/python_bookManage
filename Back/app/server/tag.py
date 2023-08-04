# coding=utf-8
""" URL: /api/panel """
from sanic import Blueprint, json

from app.utils.api import OK_Json, return_lang, CheckRequestLogin, Error_Json
from app.utils.api import return_AllLanguage as AllLanguage
from app.utils.all_time import return_DateAndTime as NowDateTime
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
tag_bp = Blueprint('tag', url_prefix='/api/index/tag')
AdminTag_bp = Blueprint('admin_tag', url_prefix='/api/admin/tag')


# 在蓝图中定义一些路由
@tag_bp.route("/list", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
@AdminTag_bp.route("/list", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def root(request):
    """获取list"""
    global Json, BooksJson
    print.INFO('* -> /api/index/tag/list')
    if request.method == 'GET':
        print.INFO(BooksJson)
        return json(OK_Json(BooksJson['Tag']), status=200)
    else:
        return json(body=ErrorRequest(), status=405)


@AdminTag_bp.route("/create", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def create(request):
    """Add"""
    global Json, BooksJson
    print.INFO('* -> /api/admin/tag/creare')
    if request.method == 'POST':
        print.INFO(BooksJson)
        TagData = {
            'title': request.form['title'][0],
            'id': BooksJson['TagID'] + 1,
            'create_time': NowDateTime()
        }
        BooksJson['TagID'] += 1
        BooksJson['Tag'].append(TagData)
        await JsonWrite(BooksJson, BooksJsonFile_Path)
        return json(OK_Json(BooksJson['Tag'], '操作成功'), status=200)
    else:
        return json(body=ErrorRequest(), status=405)

@AdminTag_bp.route("/delete", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def delete(request):
    global Json
    print.INFO('* -> /api/admin/Tag/delete')
    if request.method == 'POST':
        # print.INFO()
        DIDList = request.args.get('ids')
        DIDList = DIDList.split(',')
        print.INFO(BooksJson['Tag'])
        print.INFO(DIDList)
        BooksJson2 = []
        for a in BooksJson['Tag']:
            if str(a['id']) not in DIDList:
                print.INFO(a)
                BooksJson2.append(a)
        BooksJson['Tag'] = BooksJson2
        await JsonWrite(BooksJson, BooksJsonFile_Path)
        return json(OK_Json('', '操作成功'), status=200)
    elif request.method == 'OPTIONS':
        return json({
            "status": 200
        }, status=200)
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

