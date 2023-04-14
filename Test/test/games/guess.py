import random

def print_words(s,tag):
    if tag=="start":
        print(s.center(40, '*'))
    elif tag=="end":
        print(s.center(40, '-'))


def guess():
    tag = 'y'
    sn = 0
    en = 1000
    print_words('猜数游戏开始喽！','start')
    while tag == 'y':
        print(f'开始猜数啦，它是{sn}-{en}的数字哦')
        rand = int(random.uniform(sn, en))
        while True:
            while True:
                try:
                    num = int(input())
                    break
                except Exception:
                    print("请输入数字哦！")
            if num > rand:
                print("大了哦")
            elif num < rand:
                print("小了哦")
            elif num == rand:
                print("你猜对啦！！")
                break
            else:
                print("请输入数字！")
        print("你也太厉害了吧，再来一局吧！(继续：y  结束：n)")
        tag = input()
    print_words("关闭游戏","end")



guess()