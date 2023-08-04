# coding=utf-8
""" URL: /api/panel """
from sanic import Blueprint, json

from app.utils.api import OK_Json, NoOK_Json, return_lang, CheckRequestLogin, Error_Json, AddAllClassInClassData
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
classification_bp = Blueprint('classification', url_prefix='/api/index/classification')
AdminClassification_bp = Blueprint('admin_classification', url_prefix='/api/admin/classification')


# 在蓝图中定义一些路由
@classification_bp.route("/list", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def list(request):
    """获取list"""
    return await AdminList(request, True)

@AdminClassification_bp.route("/list", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def AdminList(request, front=False):
    """获取list"""
    global Json, BooksJson
    print.INFO('* -> /api/index/classification/list')
    if request.method == 'GET':
        print.INFO(BooksJson)
        if front:
            return json(OK_Json(AddAllClassInClassData(BooksJson['Class']), '查询成功'), status=200)
        else:
            print.INFO('rrrr')
            return json(OK_Json(BooksJson['Class'], '查询成功'), status=200)
    else:
        return json(body=ErrorRequest(), status=405)


@AdminClassification_bp.route("/create", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def create(request):
    """add"""
    global Json, BooksJson
    print.INFO('* -> /api/index/classification/list')
    if request.method == 'POST':
        addClass = request.form['title'][0]
        if addClass in BooksJson["Class"]:
            return json(NoOK_Json('已存在', 1), status=200)
        else:
            classJSON = {
                "key": BooksJson["ClassID"] + 1,
                "name": addClass,
                "title": addClass,
                "isParent": True,
                "children": []
            }
            print.INFO(BooksJson["ClassID"])
            BooksJson["ClassID"] += 1
            BooksJson['Class'].append(classJSON)
            await JsonWrite(BooksJson, BooksJsonFile_Path)
            return json(OK_Json(BooksJson['Class'], '操作成功'), status=200)
    else:
        return json(body=ErrorRequest(), status=405)

@AdminClassification_bp.route("/delete", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def delete(request):
    global Json
    print.INFO('* -> /api/admin/classification/delete')
    if request.method == 'POST':
        # print.INFO()
        DIDList = request.args.get('ids')
        DIDList = DIDList.split(',')
        print.INFO(BooksJson['Class'])
        print.INFO(DIDList)
        BooksJson2 = []
        for a in BooksJson['Class']:
            if str(a['key']) not in DIDList:
                print.INFO(a)
                BooksJson2.append(a)
        BooksJson['Class'] = BooksJson2
        await JsonWrite(BooksJson, BooksJsonFile_Path)
        return json(OK_Json('', '操作成功'), status=200)
    elif request.method == 'OPTIONS':
        return json({
            "status": 200
        }, status=200)
    else:
        return json(body=ErrorRequest(), status=405)




def new_func():
    print.INFO(BooksJson)


def SetData(data, Back_Users_Session_):
    global Data, Json, JsonFile_Path, overview_JSON, Back_Users_Session, BooksJsonFile_Path, BooksJson
    Data = data
    Json = Data.Json
    JsonFile_Path = Data.JsonFile_Path
    overview_JSON = Data.overview_JSON
    Back_Users_Session = Back_Users_Session_
    BooksJsonFile_Path = Data.BooksJsonFile_Path
    BooksJson = Data.BooksJson

