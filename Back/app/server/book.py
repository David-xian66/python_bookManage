# coding=utf-8
""" URL: /api/panel """
from sanic import Blueprint, json

from app.utils.api import OK_Json, NoOK_Json, return_lang, CheckRequestLogin, Error_Json
from app.utils.api import return_AllLanguage as AllLanguage
from app.utils.api import return_ErrorRequest as ErrorRequest
from app.utils.file import JsonWrite
from app.utils.log import Log as print
from app.utils.book import returnBookData as GetBooksData, returnBooksListData as GetBooksListData
from app.utils.book import Cheak, delete as DeleteBook, add as AddBook

Json = 'Data.Json'
JsonFile_Path = 'Data.JsonFile_Path'
overview_JSON = 'Data.overview_JSON'
Back_Users_Session = 'Back_Users_Session'
BooksJsonFile_Path = 'BooksJsonFile_Path'
BooksJson = 'BooksJson'

# 蓝图panel_bp,URL前缀'/api/panel'
book_bp = Blueprint('book', url_prefix='/api/index/book')
AdminBook_bp = Blueprint('Admin_book', url_prefix='/api/admin/book/')


# 在蓝图中定义一些路由
@book_bp.route("/list", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
@AdminBook_bp.route("/list", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def root(request):
    global Json
    print.INFO('* -> /api/index/book/list or /api/admin/book/list')
    if request.method == 'GET':
        if request.args == {}:
            BookData = await GetBooksListData(BooksJson=BooksJson)
        else:
            if 'c' in request.args:
                ClassID = request.args.get("c")
                BookData = await GetBooksListData(Class=ClassID,BooksJson=BooksJson)
            elif 'tag' in request.args:
                TagID = request.args.get("tag")
                BookData = await GetBooksListData(Tag=TagID,BooksJson=BooksJson)
        return json(OK_Json(BookData, '查询成功'), status=200)
                
    elif request.method == 'OPTIONS':
        return json({
            "status": 200
        }, status=200)
    else:
        return json(body=ErrorRequest(), status=405)
    

@book_bp.route("/detail", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def root(request):
    global Json
    print.INFO('* -> /api/index/book/detail')
    if request.method == 'GET':
        BookID = request.args.get("id")
        BookData = await GetBooksData(BookID, BooksJson)
        return json(OK_Json(BookData, '查询成功'), status=200)
                
    elif request.method == 'OPTIONS':
        return json({
            "status": 200
        }, status=200)
    else:
        return json(body=ErrorRequest(), status=405)
    






@AdminBook_bp.route("/create", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def create(request, update=False):
    global Json
    print.INFO('* -> /api/admin/book/create')
    if request.method == 'POST':
        # print.INFO()
        if Cheak(request):
            Data = {
                'title': request.form['title'][0],
                'original_title': request.form['original_title'][0],
                'classification': request.form['classification'][0],
                'cover': request.form['cover'],
                'description': request.form['description'][0],
                'author': request.form['author'][0],
                'translator': request.form['translator'][0],
                'isbn': request.form['isbn'][0],
                'price': request.form['price'][0],
                'press': request.form['press'][0],
                'layout': request.form['layout'][0],
                'page_count': request.form['page_count'][0],
                'repertory': request.form['repertory'][0],
                'status': request.form['status'][0],
                'pub_date': request.form['pub_date'][0],
                'tag': request.form['tag'],
            }
            if update:
                Data['id'] = request.args.get('id')
            await AddBook(Data, BooksJson, update)
            await JsonWrite(BooksJson, BooksJsonFile_Path)
            return json(OK_Json('', '查询成功'), status=200)
        else:
            return json(NoOK_Json('少参数'), status=200)
    elif request.method == 'OPTIONS':
        return json({
            "status": 200
        }, status=200)
    else:
        return json(body=ErrorRequest(), status=405)


@AdminBook_bp.route("/update", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def update(request):
    return await create(request, True)



@AdminBook_bp.route("/delete", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def delete(request):
    global Json
    print.INFO('* -> /api/admin/book/delete')
    if request.method == 'POST':
        # print.INFO()
        DIDList = request.args.get('ids')
        DIDList = DIDList.split(',')
        for a in DIDList:
            DeleteBook(a)
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

