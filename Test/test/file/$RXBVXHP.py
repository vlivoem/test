import time

# 时间戳转时间格式
def shijian(timeStamp):
    timeArray = time.localtime(timeStamp)
    # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime

# 时间格式转时间戳
def timestamp(shijian):
    s_t=time.strptime(shijian,"%Y-%m-%d %H:%M:%S")
    mkt=int(time.mktime(s_t))
    return(mkt)



if __name__ == "__main__":
    print(time.strptime("20220920", '%Y%m%d').tm_mday)
