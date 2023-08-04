# coding=utf-8
import os
import traceback

from sanic import Sanic
from sanic_cors import CORS
from sanic_session import Session, InMemorySessionInterface

from app.server.book import book_bp, AdminBook_bp, SetData as SetData_Book
from app.server.classification import classification_bp, AdminClassification_bp, SetData as SetData_Classification 
from app.server.tag import tag_bp, AdminTag_bp, SetData as SetData_Tag
from app.server.overview import overview_bp, SetData as SetData_Overview
from app.server.notice import notice_bp, SetData as SetData_Notice
from app.server.user import users_bp, BackUsers_bp, SetData as SetData_User
from app.server.root import root_bp, SetData as SetData_Root
from app.settings import Data
from app.utils.file import JsonRead_NotAsync
from app.utils.log import Log as print, Sanic_Log

app = Sanic("MSS_Back", log_config=Sanic_Log)
app.config.FALLBACK_ERROR_FORMAT = "json"
app.config.REQUEST_MAX_HEADER_SIZE = 4194304
CORS(app)

session = Session(app, interface=InMemorySessionInterface())
JsonFile_Path = os.path.join('config.json')

try:
    Json = JsonRead_NotAsync(os.path.join('config.json'))
except FileNotFoundError:
    Json = ''
except:
    traceback.format_exc()
    
BooksJsonFile_Path = os.path.join('Books','config.json')
BooksJson = {}

try:
    BooksJson = JsonRead_NotAsync(BooksJsonFile_Path)
except FileNotFoundError:
    BooksJson = ''
except:
    traceback.format_exc()


Data.app = app
Data.session = session
Data.Json = Json
Data.JsonFile_Path = JsonFile_Path
Back_Users_Session = {}
Data.BooksJsonFile_Path = BooksJsonFile_Path
Data.BooksJson = BooksJson


# app_server_File.SetData(Data)

def SetData_(data):
    SetData_User(data, Back_Users_Session)
    SetData_Overview(data, Back_Users_Session)
    SetData_Book(data, Back_Users_Session)
    SetData_Classification(data, Back_Users_Session)
    SetData_Tag(data, Back_Users_Session)
    SetData_Notice(data, Back_Users_Session)
    SetData_Root(data, Back_Users_Session)


SetData_(Data)

app.blueprint(users_bp)
app.blueprint(overview_bp)
app.blueprint(BackUsers_bp)
app.blueprint(classification_bp)
app.blueprint(AdminClassification_bp)
app.blueprint(tag_bp)
app.blueprint(AdminTag_bp)
app.blueprint(AdminBook_bp)
app.blueprint(book_bp)
app.blueprint(notice_bp)
app.blueprint(root_bp)


def Start(IP, Port):
    try:
        app.run(host=IP, port=Port, debug=False, auto_reload=True, fast=False)
    except OSError:
        exit(0)


def Start_Run_SetData():
    global app, JsonFile_Path, Json, BooksJson, BooksJsonFile_Path, Data
    app.blueprint(users_bp)
    app.blueprint(overview_bp)
    app.blueprint(BackUsers_bp)
    app.blueprint(AdminBook_bp)
    app.blueprint(book_bp)
    app.blueprint(AdminClassification_bp)
    app.blueprint(classification_bp)
    app.blueprint(AdminTag_bp)
    app.blueprint(tag_bp)
    app.blueprint(notice_bp)
    app.blueprint(root_bp)

    JsonFile_Path = os.path.join('config.json')
    # try:
    # Json = JsonRead_NotAsync(JsonFile_Path)
    # BooksJson = JsonRead_NotAsync(BooksJsonFile_Path)
    # except:
    #     pass


def Start_Run(IP_, Post_):
    global IP, Post
    IP = IP_
    Post = Post_
    Data.IP = IP
    Data.Post = Post
    print.INFO('ss')
    SetData_(Data)
    Start_Run_SetData()
    Start(IP, Post)

