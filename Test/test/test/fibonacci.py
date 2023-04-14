def fibonacci(num=10):
    num = num - 1
    f1 = 0
    f2 = 1
    while num:
        print(f1, end=',')
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        num -= 1
    print(f1)


# fibonacci(20)


def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


# print(fib(3))

def read(ab):
    for i in ab:
        print(i, end=' ')
    print()





# a = ['12','sdf','---']
# b = a
# print("a:",end="")
# read(a)
# print("b:",end="")
# read(b)
# a = '1111'
# print('修改列表a后：')
# print("a:",end="")
# read(a)
# print("b:",end="")
# read(b)
# print("列表赋值为值传递！")