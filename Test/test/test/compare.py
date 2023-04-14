def compare(re=0):
    numbers = []
    numbers_sort = []

    # 接受输入的数字
    while True:
        num = input("请输入数字，以-999结束输入：")
        # 判断结束条件
        if num == "-999":
            break
        else:
            # 判断非数字情况
            try:
                num = float(num)
            except:
                print("请输入正确的数字！")
                continue
        # 判断是否为整数
        if int(num) == num:
            num = int(num)
        numbers.append(num)

    # 对列表中的数字进行排序
    for num1 in numbers:
        tag = 0
        for num2 in numbers_sort:
            if num1 < num2:
                numbers_sort.insert(numbers_sort.index(num2), num1)
                tag = 1
                break
        if tag == 0:
            numbers_sort.append(num1)

    # 输出排序前的列表
    print("你输入的数字列表为：", end='')
    for i in numbers:
        print(str(i) + ' ', end=' ')

    # 正序还是逆序
    if re == 1:
        numbers_sort.reverse()

    # 输出排序后的内容
    print("\n排序后：", end='')
    for i in numbers_sort:
        if i == numbers_sort[0]:
            print(str(i), end='')
        elif re == 1:
            print('>' + str(i), end='')
        else:
            print('<' + str(i), end='')


compare()
