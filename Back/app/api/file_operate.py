# coding=utf-8
import os


#
# def FileWalk_Page(fileList: list, quantity=False, page=1, maxQuantity=False):
#     """处理文件列表的Page问题"""
#     fileList_len = len(fileList)
#     if maxQuantity and fileList_len > maxQuantity:
#         # 如果设置了最大多少
#         # 并且超过上线
#         return [False, fileList_len]
#     else:
#         page_ = 1
#         if quantity and fileList_len > quantity:
#             # 如果设置了返回多少,并且超过了这个数目,就进行截取
#             if page == 1:
#                 fileList = fileList[:quantity]
#                 #print(quantity)
#             else:
#                 #print(page * quantity - quantity)
#                 #print(page * quantity)
#                 fileList = fileList[page * quantity - quantity:page * quantity]
#
#             # 计算一共几页
#             dm = divmod(fileList_len, quantity)
#             if dm[1] == 0:  # 如果余数是0
#                 page_ = dm[0]
#             else:
#                 page_ = dm[0] + 1
#
#         return [True, page_, fileList]


"""
async def main():
    directory = './my_folder'
    files_list = await list_files(directory)
    print(files_list)

asyncio.run(main())


import zipfile

# 打开ZIP文件
with zipfile.ZipFile('example.zip', 'r') as zip_file:
    # 列出ZIP文件中的所有文件和目录
    zip_file.printdir()
    
    # 读取ZIP文件中的文本文件
    with zip_file.open('example.txt') as txt_file:
        text = txt_file.read()
        print(text.decode('utf-8'))
"""
