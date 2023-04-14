import os
from test.file.delefile.mine import *
# from mine import *
# from datetime import datetime
# import time
#
# dir0 = os.getcwd()
#
# file_list = os.listdir(dir0)
#
# for f in file_list:
#     date = shijian(os.path.getmtime(f))
#     print(date, end="    ")
#     print(os.path.getmtime(f))
#
#
# print(time.time())
#
#
#




# 修改指定文件夹及其子文件夹的修改日期
def a(path):
    # 进入指定文件夹
    os.chdir(path)
    # 获取当前文件夹下的文件列表
    for f in os.listdir(os.getcwd()):
        # 如果当前文件名为一个目录
        if os.path.isdir(f):
            # 递归调用本函数，排查子文件夹下的文件
            a(path + '/' + f)
            # 当上一步递归调用结束后，需改变当前文件夹至当前文件夹的父文件夹
            os.chdir(os.getcwd()[0:os.getcwd().rfind('/')])
        # 将时间更改为时间戳格式
        create = timestamp("2021-06-03")
        update = timestamp("2021-06-04")
        # 修改文件的修改时间
        os.utime(f, (create, update))


if __name__ == "__main__":
    a(os.getcwd())

