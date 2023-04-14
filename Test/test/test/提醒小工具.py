from win10toast import ToastNotifier
import time

def alert():
    toaster = ToastNotifier()
    try:
        # 获取提醒弹框的标题
        header = input("Title of reminder: ")
        # 获取提醒弹框的信息
        text = input("Message of reminder: ")
        # 获取提醒的时间：多少分钟后
        time_min = input("In how many minutes: ")
        time_min = float(time_min)
    except:
        header = input("Title of reminder: ")
        text = input("\nMessage of remindar: ")
        time_min = float(input("\nIn how many minutes: "))
    # 将分钟转换成秒
    time_min = time_min * 60
    print("Setting up reminder..")
    time.sleep(2)
    print("all set!")
    time.sleep(time_min)
    toaster.show_toast(f"{header}",
    f"{text}",
    duration=10,
    threaded=True)
    while toaster.notification_active():time.sleep(0.005)


if __name__ == "__main__":
    alert()