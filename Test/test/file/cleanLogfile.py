
# coding=UTF-8
# This Python file uses the following encoding: utf-8

import os
import sys
from datetime import time

from test.file import mine

# 获取当前时间
nowDate = time.strftime('%Y%m%d')
# 给一个时间默认值
lens = 90
# 定义删除列表
deleteArr = []

# 获取创建时间至今的天数
def days(str1, str2):
    # 从时间字符串中获取日期进行比较
    date1 = int(str1[6:])
    date2 = int(str2[6:])
    if date1 < date2:
        d = 0
    else:
        d = date1 - date2
    # 算出创建时间至今的天数，，，，粗略估计每月为30天，后期优化
    num = d + months(str1,str2)*30
    return num

# 获取创建时间至今的天数--计算月与年的部分
def months(str1, str2):
    # 从字符串中获取年月
    year1 = int(str1[0:4])
    year2 = int(str2[0:4])
    month1 = int(str1[4:6])
    month2 = int(str2[4:6])
    # 比较年月，并进行对应处理
    if year1 < year2:
        y = 0
    else:
        y = year1 -year2
    if month1 < month2:
        m = 12 - (month2 - month1)
    else:
        m = month1 - month2
    # 计算距今多少个月，用于计算天数
    num = y * 12 + m
    return num

# 递归判断文件夹中的文件是否满足要求
def foreach(path):
    # 定义全局变量 删除文件列表
    global deleteArr
    # 跳转到要判断的文件夹
    os.chdir(path)
    print("查询路径"+path+"...")
    # 迭代，判断当前路径下的文件是否满足要求
    for fileobj in os.listdir(path):
        # 判断文件名是否为文件夹
        if os.path.isdir(fileobj):
            # 若为文件夹则递归改文件夹
            foreach(path + '/' + fileobj)
            # 该文件夹递归完成后需返回父文件夹
            os.chdir(os.getcwd()[0:os.getcwd().rfind('/')])
            # 如果需要将空文件夹一起删除的话，放开下面这条
            # deleteArr.append(path + '/' + fileobj)
        else:
            # 获取文件的修改时间，并转换为时间格式字符串
            logFileTime = shijian(os.path.getmtime(path+"/"+fileobj)).replace('-', '')
            # 获取文件修改时间正常
            if len(logFileTime) > 0:
                # 获取至今天数
                day = days(nowDate, logFileTime)
                # 若大于给定天数
                if day > lens:
                    # 将符合要求的文件添加到删除列表中
                    if fileobj != os.path.basename(sys.argv[0]):
                        deleteArr.append(path + '/' + fileobj)
    return deleteArr


# 删除文件
def deleFile(filePath):
    print("正在删除文件：" + filePath)
    # 删除文件夹，，如果有的话
    if os.path.isdir(filePath):
        try:
            os.rmdir(filePath)
        except:
            print("文件夹"+filePath+"删除失败！")
    else:
        os.remove(filePath)

# 流程控制
def manfun(*arr):
    # 使用全局变量，删除天数
    global lens
    # 默认第一个传参为删除路径
    path = arr[1]
    # print(arr)
    # 根据可变参数列表的长度处理各传参
    if len(arr) == 2:
        # 当传参为2时，判断输入的路径是否正确
        if not os.path.isdir(path):
            print('请输入正确的文件夹目录!')
            print('文件执行格式（解释器 文件名 删除文件路径）：python cleanLogfile.py /data/dev_apps/order-pay/logs')
            print('文件执行格式（解释器 文件名 删除文件路径 删除时间）：python cleanLogfile.py /data/dev_apps/order-pay/logs 90')
        # 当传参为3时，判断
    elif len(arr) == 3:
        if not isinstance(arr[2], int):
            print('请输入正确的文件夹目录!')
            print('文件执行格式（解释器 文件名 删除文件路径）：python cleanLogfile.py /data/dev_apps/order-pay/logs')
            print('文件执行格式（解释器 文件名 删除文件路径 删除时间）：python cleanLogfile.py /data/dev_apps/order-pay/logs 90')
        else:
            lens = int(arr[2])
    else:
        print('请输入正确的文件夹目录!')
        print('文件执行格式（解释器 文件名 删除文件路径）：python cleanLogfile.py /data/dev_apps/order-pay/logs')
        print('文件执行格式（解释器 文件名 删除文件路径 删除时间）：python cleanLogfile.py /data/dev_apps/order-pay/logs 90')
    for filePath in foreach(path):
        deleFile(filePath)
    print("合规删除数据：", len(deleteArr), deleteArr)


if __name__ == '__main__':
    manfun(sys.argv, os.getcwd(), 1)


