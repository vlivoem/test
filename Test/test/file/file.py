import os
import random
import re

## if os.path.exists('txt.txt'):
#     fo = open('txt.txt', 'r',encoding='utf-8')
#     file = open('file.txt', 'a')
#     file.truncate(0)
#     while True:
#         line = fo.readline()
#         if len(line) == 0:
#             break
#         file.write(line)
#     fo.close()
#     file.close()
import time


def get_file_to_list(file):
    if os.path.exists(file):
        f = open(file)
        list1 = []
        while True:
            line = f.readline()
            # 去除多余内容
            line = re.sub(r'\d+、', '', line)
            list1.append(line)
            if len(list1[list1.__len__() - 1]) == 0:
                break
        f.close()
        return list1

if __name__ == "__main__":
    list1 = get_file_to_list('file.txt')
    words = list1[random.randint(0, list1.__len__() - 1)].strip('     ')
    print(f'每日一句：\n{words}')

    with open("file.log", 'a') as file:
        file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '   成功运行文件一次，输出内容为：' + words)
