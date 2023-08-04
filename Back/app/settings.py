# coding=utf-8


# 变量共享

class Data:
    Json = None
    JsonFile_Path = None
    overview_JSON = {
        'CPU': [],
        'RAM': []
    }
    overview_Thread = ''
    session = ''
    app = None
    IP = ''
    Post = -1
    BooksJson = None
    BooksJsonFile_Path = None

# Data_ = Data

# def SetData(data):
#       global Data
