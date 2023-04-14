import time
from math import sqrt


# 九九乘法表
def jiu():
    """打印九九乘法表"""
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(j) + '*' + str(i) + '=' + str(i * j), end="\t")
        time.sleep(1)
        print()


# jiu()

# 当前日期的格式
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


# 小兔子生兔子
def rabbit(n):
    """小兔子问题：一对小兔子，每对三个月后每个月生一对"""
    f1 = 1
    f2 = 1
    for i in range(1, n):
        print('%12ld %12ld' % (f1, f2), end=" ")
        if (i % 3) == 0:
            print('')
        f1 = f1 + f2
        f2 = f1 + f2


def suShu(num):
    """判断一个数字是否是素数"""
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            # print(str(num) + "不是素数！")
            return 0
    else:
        # print(str(num) + "是素数！")
        return 1


# sushu(9)
# sushu(10)
# sushu(5)


def shuiXianHua(min0=100, max0=999):
    """输出min到max之间的水仙花数"""
    try:
        if (min0 < 100) | (max0 > 999) | (min0 > max0):
            print("传参错误！")
            return
    except:
        print("传参错误！")
        return
    for n in range(min0, max0+1):
        a = int(n / 100)
        b = int(n / 10 % 10)
        c = n % 10
        if n == a * a * a + b * b * b + c * c * c:
            print(n, end="\t")

def reduceNum(n):
    """分解质因数"""
    for i in range(2,n-1):
        if n%i ==0:
            print(i,end='*')
            n = int(n/i)
            reduceNum(n)
            break
    else:
        print(n)

# def reduceNum(n):
#     print ('{} = '.format(n), end=" ")
#     if not isinstance(n, int) or n <= 0 :
#         print ('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1] :
#         print ('{}'.format(n))
#     while n not in [1] : # 循环保证递归
#         for index in range(2, n + 1) :
#             if n % index == 0:
#                 n //= index # n 等于 n//index
#                 if n == 1:
#                     print (index )
#                 else : # index 一定是素数
#                     print ('{} *'.format(index), end=" ")
#                 break


