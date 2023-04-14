from test.database.pymysql_connect import mysql_test
from test.database.student import student

# 使用 cursor() 方法创建一个游标对象 cursor
db = mysql_test()
cursor = db.cursor()


def create_datebase():
    """创建数据表"""

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS student_info")

    # 使用预处理语句创建表
    sql = """CREATE TABLE student_info (
             first_name  CHAR(20) NOT NULL,
             last_name  CHAR(20),
             age INT,  
             sex CHAR(1),
             class CHAR(20) )"""

    result = cursor.execute(sql)
    print(result)
    db.close()


def insert_info():
    """插入数据"""
    num=0
    rj1181 = [student('wj', 'l', 20, 'f'), student('sf', 'l', 19, 'f'), student('zm', 'w', 19, 'f')]
    for i in rj1181:
        i.cla = '软件1181'
    for stu in rj1181:
        # SQL 插入语句
        sql = """INSERT INTO student_info(first_name,
             last_name, age, sex, class)
             VALUES ('%s','%s','%s','%s','%s')""" % (stu.first_name, stu.last_name, stu.age, stu.sex, stu.cla)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            num=num+1
        except:
            # 如果发生错误则回滚
            db.rollback()
    # 关闭数据库连接
    db.close()
    print(f'已插入{num}条数据。')

# insert_info()
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
