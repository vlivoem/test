import re

while True:
    st = input("请输入需要判断的日期（示例：20220926）")
    if not re.match(r'^\d{8}$',st):
        print("请输入正确格式的日期！")
        continue
    year = int(st[0:4])
    month = int(st[4:6])
    day = int(st[6:8])
    print("年： " + str(year))
    print("月： " + str(month))
    print("日: " + str(day))

    day0 = 30
    months = [1,3,5,7,8,10,12]
    if month in months:
        day0 = 31
    elif month == 2:
        if(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            day0 = 28
        else:
            day0 = 29

    if month > 12 | month < 1:
        print("请输入正确的月份！")
        continue
    elif day > day0 | day < 1:
        print("请输入正确的日期！")
        continue

    sum = 0
    for m in range(1, month):
        if m in months:
            sum += 31
        elif m == 2:
            if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
                sum += 28
            sum += 29
        else:
            sum += 30

    sum += day

    print(str(st) + "是当年的第" + str(sum) + "天。")


    n = input("是否需要继续，请输入Y/N:")
    if n in 'nN':
        break