import os
import pandas as pd
import openpyxl
# excel1 = input("请输入表1的名称:")
excel1 = "D:\lwj\data.xlsx"
excel2 = "D:\lwj\data2.xlsx"
data1_deviceId = []
data1_deviceName = []
data2_deviceId = []
notData2 = []
if os.path.exists(excel1) and os.path.exists(excel2):
    data1 = pd.read_excel(excel1)
    data2 = pd.read_excel(excel2)['DeviceId']
    for deviceId in data1['DeviceId']:
        data1_deviceId.append(deviceId)
    for deviceId in data2:
        data2_deviceId.append(deviceId)
    for name in data1["DeviceName"]:
        data1_deviceName.append(name)

    for deviceId in data1_deviceId:
        if deviceId not in data2_deviceId:
            notData2.append([deviceId, data1_deviceName[data1_deviceId.index(deviceId)]])
else:
    print("文件不可打开")

print("data1中有data2中没有的：\n设备id\t\t\t\t\t设备名称")
for device in notData2:
    print(device[0] + "\t" + device[1])


