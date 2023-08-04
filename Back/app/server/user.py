# coding=utf-8
""" URL: /api/index/user """
from sanic import Blueprint, json

# from app.settings import Json, JsonFile_Path
from app.utils.algorithm_data import NewUUID, HMAC_New, NewMD5
from app.utils.all_time import return_DateAndTime as NowDateTime
from app.utils.all_time import return_Time as NowTime
# from app.utils.api import passwordCheck
from app.utils.api import return_ErrorRequest as ErrorRequest, CheckRequestLogin, OK_Json, NoOK_Json
from app.utils.file import JsonWrite
from app.utils.log import Log as print


Json = 'Data.Json'
JsonFile_Path = 'Data.JsonFile_Path'
overview_JSON = 'Data.overview_JSON'
Back_Users_Session = 'Back_Users_Session'
BooksJsonFile_Path = 'BooksJsonFile_Path'
BooksJson = 'BooksJson'

# 蓝图users_bp,URL前缀'/users'
users_bp = Blueprint('user', url_prefix='/api/index/user')
BackUsers_bp = Blueprint('back_user', url_prefix='/api/admin/adminLogin')

@users_bp.route("/register", methods=["GET", "POST", "PUT", "DELETE"])
async def api_user_init(request):
    """用户注册"""
    global Json
    print(Json)
    print.INFO('* -> /api/index/user/register')
    if request.method == 'POST':
        username = request.json['username']
        if username not in Json['Front_Users']:
            password = request.json['password']
            repassword = request.json['repassword']
            # if passwordCheck(password):
                # 如果验证通过
            if repassword == password:
                # 检查两个密码是否相等
                password = NewMD5(password)
                password_K = HMAC_New(password, password)
                id = len(Json['Front_Users']) + 1
                T = NowDateTime()
                
                Json['Front_Users'][username] = {
                    'username': username,
                    'password': password_K,
                    'id': id,
                    'create_time': T,
                    "role": "2",
                    "status": "0",
                    "nickname": None,
                    "avatar": None,
                    "mobile": None,
                    "email": None,
                    "gender": None,
                    "description": None,
                    "score": 0,
                    "push_email": None,
                    "push_switch": False,
                    "admin_token": None,
                    "token": None,
                    # 'lastLoginTime': T,
                    'permission': {
                        "ban": False
                    }
                }
                print.INFO(Json)
                await JsonWrite(Json, JsonFile_Path)
                return json(OK_Json(Json['Front_Users'][username], "创建成功"), status=200)
            else:
                return json(NoOK_Json("密码不一致", 1), status=405)
        else:
            return json(NoOK_Json("该用户名已存在", 1), status=405)
    else:
        return json(body=ErrorRequest(), status=405)


@users_bp.route("/login", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def api_user_login(request):
    """用户登录"""
    global Json
    print.INFO('* -> /api/user/login')
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        if username in Json['Front_Users']:
            password = NewMD5(password)
            password = HMAC_New(password, password)
            print.INFO(password)
            print.INFO(Json['Front_Users'][username]['password'])
            if Json['Front_Users'][username]['password'] == password:
                sid = request.ctx.session.sid
                if sid in Back_Users_Session:
                    if int(NowTime()) < Back_Users_Session[sid]['expirationTime']:
                        # 如果没失效
                        Back_Users_Session[sid]['expirationTime'] = int(NowTime()) + 86400
                    else:
                        # 如果失效了
                        Back_Users_Session[sid]['expirationTime'] = int(NowTime()) + 86400
                else:
                    # 如果是新的ID
                    Back_Users_Session[sid] = {
                        'expirationTime': int(NowTime()) + 86400,
                        'UserName': username
                    }
                Json['Front_Users'][username]['registerTime'] = NowDateTime()
                Json['Front_Users'][username]['token'] = Json['Front_Users'][username]['admin_token'] = sid                # await JsonWrite(Json, JsonFile_Path)
                response = json(OK_Json(Json['Front_Users'][username], "登录成功"), status=200)
                response.cookies['session'] = sid
                await JsonWrite(Json, JsonFile_Path)
                return response
            else:
                return json(NoOK_Json("用户名或密码错误", 1), status=200)
        else:
            return json(NoOK_Json("用户名或密码错误", 1), status=200)
    else:
        return json(body=ErrorRequest(), status=405)


@BackUsers_bp.route("/", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def api_user_login(request):
    """用户登录"""
    global Json
    print.INFO('* -> /api/admin/adminLogins')
    if request.method == 'POST':
        username = request.form['username'][0]
        password = request.form['password'][0]
        
        if username == 'admin123' and password == 'admin123' and len(Json['Back_Users']) == 0:
            # 如果默认账号没注册,并且密码正确
            password = NewMD5(password)
            password_K = HMAC_New(password, password)
            T = NowDateTime()
            id = len(Json['Back_Users']) + 1
            Json['Back_Users'][username] = {
                'username': username,
                'password': password_K,
                'id': id,
                'create_time': T,
                "role": "0",
                "status": "0",
                "nickname": None,
                "avatar": None,
                "mobile": None,
                "email": None,
                "gender": None,
                "description": None,
                "score": 0,
                "push_email": None,
                "push_switch": False,
                "admin_token": None,
                "token": None,
                # 'lastLoginTime': T,
                'permission': {
                        "ban": False
                }
            }
            sid = request.ctx.session.sid
            if sid in Back_Users_Session:
                if int(NowTime()) < Back_Users_Session[sid]['expirationTime']:
                        # 如果没失效
                        Back_Users_Session[sid]['expirationTime'] = int(NowTime()) + 86400
                else:
                    # 如果失效了
                    Back_Users_Session[sid]['expirationTime'] = int(NowTime()) + 86400
            else:
                        # 如果是新的ID
                Back_Users_Session[sid] = {
                    'expirationTime': int(NowTime()) + 86400,
                    'UserName': username
                }
            Json['Back_Users'][username]['registerTime'] = NowDateTime()
            Json['Back_Users'][username]['token'] = Json['Back_Users'][username]['admin_token'] = sid
            response = json(OK_Json(Json['Back_Users'][username], "登录成功"), status=200)
            response.cookies['session'] = sid
            await JsonWrite(Json, JsonFile_Path)
            return response
        else:
            if username in Json['Back_Users']:
                password = NewMD5(password)
                password = HMAC_New(password, password)
                print.INFO(password)
                print.INFO(Json['Back_Users'][username]['password'])
                if Json['Back_Users'][username]['password'] == password:
                    sid = request.ctx.session.sid
                    if sid in Back_Users_Session:
                        if int(NowTime()) < Back_Users_Session[sid]['expirationTime']:
                            # 如果没失效
                            Back_Users_Session[sid]['expirationTime'] = int(NowTime()) + 86400
                        else:
                            # 如果失效了
                            Back_Users_Session[sid]['expirationTime'] = int(NowTime()) + 86400
                    else:
                        # 如果是新的ID
                        Back_Users_Session[sid] = {
                            'expirationTime': int(NowTime()) + 86400,
                            'UserName': username
                        }
                    Json['Back_Users'][username]['registerTime'] = NowDateTime()
                    Json['Back_Users'][username]['token'] = Json['Back_Users'][username]['admin_token'] = sid                # await JsonWrite(Json, JsonFile_Path)
                    response = json(OK_Json(Json['Back_Users'][username], "登录成功"), status=200)
                    response.cookies['session'] = sid
                    await JsonWrite(Json, JsonFile_Path)
                    return response
                else:
                    return json(NoOK_Json("用户名或密码错误", 1), status=200)
            else:
                return json(NoOK_Json("用户名或密码错误", 1), status=200)
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
