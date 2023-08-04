# coding=utf-8
import asyncio
import json
import os
import aiofiles
from app.utils.file import JsonRead, JsonWrite, DeletePath
from app.utils.img import CheakAndSaveImg_ReturnPath


async def returnBooksListData(Class=None, Tag=None, BooksJson=None):
    """得到书的listData"""
    bookDataList = []
    path = os.path.join('Books')
    
    # 如果过滤Class/Tag
    # 先找到Class/Tag对应ID
    Class = UseClassIDFindClassName(Class, BooksJson)
    Tag = UseTapIDFindTapName(Tag, BooksJson)
    
    for bookFileName in os.listdir(path):
        bookFileNamePath = os.path.join(path,bookFileName)
        if os.path.isdir(bookFileNamePath):
            bookJSONPath = os.path.join(bookFileNamePath, 'config.json')
            if os.path.isfile(bookJSONPath):
                # 如果config配置文件存在
                bookJSONData = await JsonRead(bookJSONPath)
                if Class:
                    # 如果Class不是None（设置了过滤Class）
                    if bookJSONData['classification'] == Class:
                        bookDataList.append(bookJSONData)
                elif Tag and bookJSONData['tag']:
                    # 如果Tag不是None（设置了过滤Tag）
                    if Tag in bookJSONData['tag']:
                        bookDataList.append(bookJSONData)
                else:
                    bookDataList.append(bookJSONData)
    return bookDataList 

async def returnBookData(BookID, BooksJson):
    """得到书的Data"""
    path = os.path.join('Books', str(BookID), 'config.json')
    
    bookJSONData = await JsonRead(path)
                
    return bookJSONData 




def UseClassIDFindClassName(ClassID, BooksJson):
    Name = None
    if ClassID:
        for a in BooksJson['Class']:
            if a['key'] == int(ClassID):
                Name = a['name']
                break
        print(Name)
        return Name
    else:
        pass

def UseTapIDFindTapName(TapID, BooksJson):
    Name = None
    if TapID:
        for a in BooksJson['Tag']:
            if a['id'] == int(TapID):
                Name = a['title']
                break
        print(Name)
        return Name
    else:
        pass

async def add(DataJson, BookJson, update):
    """add book"""
    path = os.path.join('Books')
    if update:
        id = DataJson['id']
    else:
        id = str(BookJson['BookID'] + 1)
    bookFileName = os.path.join(path, id)
    bookFileJSON =  os.path.join(bookFileName, 'config.json')
    
    # 文件检查
    if not os.path.isdir(bookFileName):
        os.mkdir(bookFileName)
        
    DataJson['cover'] = await CheakAndSaveImg_ReturnPath(DataJson['cover'], bookFileName, id)
    
    # 修正Class的值
    try:
        DataJson['classification'] = UseClassIDFindClassName(DataJson['classification'], BookJson)
    except ValueError:
        pass
    
    # 修正Tag的值
    tag2 = []
    for a in DataJson['tag']:
        tag2.append(UseTapIDFindTapName(a, BookJson))
    DataJson['tag'] = tag2
    
    
    # 修正id的值
    DataJson['id'] = id
    
    print(DataJson['cover'])
    #  writeJSONFile
    BookJson['BookID'] += 1
    await JsonWrite(DataJson, bookFileJSON)
    return True 


def delete(id):
    """delete book"""
    path = os.path.join('Books')
    bookFileName = os.path.join(path, id)
    DeletePath(bookFileName)
    return True 



def Cheak(request):
    if 'title' in request.form:
        CheakList = [
            'original_title',
            'classification',
            # 'cover',
            'description',
            'author',
            'translator',
            'isbn',
            'price',
            'press',
            'layout',
            'page_count',
            'repertory',
            'status',
            'pub_date',
            'tag',
        ]
        for c in CheakList:
            if c not in request.form:
                request.form[c] = [None]
        if 'cover' not in request.files:
            request.form['cover'] = None
        else:
            request.form['cover'] = request.files['cover'][0].body
        return True
    else:
        return False

if __name__ == '__main__':
    tasks = [
        asyncio.ensure_future(find())
    ]
        
    # 协程函数使用 func1()这种方式是执行不了的
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))