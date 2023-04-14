import pymysql
# 打开数据库连接

def mysql_test():
    db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    return db