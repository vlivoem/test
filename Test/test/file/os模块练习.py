# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime

# 按时间创建文件夹
def creat_dir_as_time(path = "d:/lwj/os_test",year1=2020,year2=2023):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    # print(os.getcwd())
    # 按时间创建文件夹
    for year in range(year1,year2+1):
        os.mkdir(str(year))
        os.chdir(str(year))
        for month in range(1,13):
            os.mkdir(str(month))
            os.chdir(str(month))
            for day in range(1,32):
                # 跳过特殊情况
                if month in (2, 4, 6, 9, 12) and day == 31:
                    continue
                if month == 2 and day == 30:
                    continue
                if month == 2 and day == 29 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                    continue
                os.mkdir(str(day))
            # 返回上级目录
            os.chdir(os.path.dirname(os.getcwd()))
        # 返回上级目录
        os.chdir(os.path.dirname(os.getcwd()))
    # print(os.getcwd())
    # 返回值为创建的路径
    return os.getcwd()

# 按时间将文件分类存放 path1为文件路径，path2为目的路径
def cp_file(path1 = "D:\lwj\相关账号",path2 = "d:/lwj/os_test"):
    # 如果时间路径不存在，创建路径
    if not os.path.exists(path2):
        path2 = creat_dir_as_time()
    if not os.path.exists(path1) or not os.path.exists(path2):
        print("路径不存在！")
        return False
    os.chdir(path1)
    files_list = os.listdir(os.getcwd())
    # 当文件为空时，返回上级目录
    if len(files_list) == 0:
        os.chdir(os.path.dirname(os.getcwd()))
    else:
        # 逐个读取文件
        for file in files_list:
            # 获取当前文件路径，并统一路径格式（读取时返回分隔符/，使用路径时需用\）
            file_path = (os.getcwd()+"\\"+file).replace("\\","\\")
            # 当获取到的文件名为文件夹时
            if os.path.isdir(file_path):
                # 递归调用，排查路径
                cp_file(file_path, path2)
            # 当获取到的文件名为文件时
            if os.path.isfile(file_path):
                # 获取文件创建时间,并将时间戳转换为时间格式
                file_time = datetime.fromtimestamp(os.path.getctime(file_path))
                # 将时间格式转换为可识别的字符串
                date_str = datetime.strftime(file_time, "%Y-%m-%d").split("-")
                # 因创建日期文件夹格式中的月与日均无0开头，需删除掉从创建文件时间中获取到的开头的0
                if date_str[1]!=10 and '0' in date_str[1]:
                    date_str[1]=date_str[1].replace("0","")
                if date_str[2]!=10 and date_str[2]!=20 and date_str[2]!=30 and '0' in date_str[1]:
                    date_str[2] = date_str[2].replace("0", "")
                # 组装待复制的路径
                copy_path = (path2 + "/" + date_str[0] + "/" + date_str[1] + "/" + date_str[2] + "/"+file).replace("/","\\")
                commd = "copy %s %s" % (file_path, copy_path)
                print(commd)
                os.system(commd)
                if os.path.isfile(copy_path):
                    print("复制成功")
            # 当文件为当前目录中的最后一个文件时，返回上级目录
            if file == files_list[len(files_list) - 1]:
                os.chdir(os.path.dirname(os.getcwd()))


# 按文件名查询文件
def find_file_by_name(file_path, name, copy_path="d:/lwj/os_test"):
    # 判断文件路径是否存在
    if os.path.isdir(file_path):
        # 存在则进入文件路径
        os.chdir(file_path)
        # print(file_path)
    else:
        print("路径不存在")
    # 目标路径不存在时创建一个
    if not os.path.isdir(copy_path):
        os.mkdir(copy_path)
    file_list = os.listdir()
    # 路径为空时返回上一级目录
    if len(file_list) == 0:
        os.chdir(os.path.dirname(os.getcwd()))
    else:
        # 遍历文件列表
        for file in file_list:
            # 转化路径格式
            file_path = (os.getcwd() + "\\" + file).replace("/","\\")
            copy_path = copy_path.replace("/","\\")
            # 文件名为路径时，递归进入
            if os.path.isdir(file):
                find_file_by_name(file_path, name, copy_path)
            # 文件名为文件时，拷贝文件进目标目录
            if os.path.isfile(file) and (name in file):
                commd = "copy %s %s" % (file_path,copy_path)
                print(commd)
                os.system(commd)
            # 当文件列表遍历完成时，返回上一级目录
            if file == file_list[len(file_list)-1]:
                os.chdir(os.path.dirname(os.getcwd()))


if __name__ == "__main__":
    # cp_file()
    # find_file_by_name("D:\lwj\生产文件", ".zip")
    # print("执行成功")
    str = "00000123456"
    print(re.sub(r'0', "", str))