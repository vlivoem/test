import os


# def list_dir(path, list_name):  # 传入存储的list
#     for file in os.listdir(path):  # os.listdir(path)，路径下的文件及文件夹，不包含子文件和子文件夹
#         file_path = os.path.join(path, file)
#         if os.path.isdir(file_path):  # 判断是否目录
#             list_dir(file_path, list_name)
#         else:
#             list_name.append(file_path)
#
#
# # fileList = []
# # list_dir("d:\\aaa", fileList)
# # print(fileList)
#
#
# def file_name(file_dir):
#     for dirs in os.walk(file_dir):
#         print(dirs)  # 当前目录路径（包含所有子目录）
#
#
# dir0 = "d:\\aaa"
# # file_name(dir0)
# print('---------------------------------------------------')
#
# def listdir(file_dir):
#     for file in os.listdir(file_dir):
#         d = file_dir+'\\'+file
#         if os.path.isdir(d):
#             print(file+"")
#             os.chdir(d)
#             listdir(d)
#         else:
#             print(file)
#
#
# listdir(dir0)
# print('---------------------------------------------------')
#
#
#

print(os.access("d:\\aaa", os.X_OK))