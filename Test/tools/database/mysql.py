import configparser

import pymysql

from tools.database import get_config
from tools.database.student import student


# 打开数据库连接
def mysql_connect():
    """打开数据库连接
        参数：
           host 数据库地址，类型为string
           port 端口号，类型为int
           user 用户名，类型为string
           passwd 密码，类型为string
           db_name 数据库名称，类型为string
    """
    # 获取配置文件中的配置
    config = get_config.get_config('mysql')
    try:
        # 使用配置文件中的数据库信息
        db = pymysql.connect(host=config['host'],
                         port=int(config['port']),
                         user=config['user'],
                         passwd=config['password'],
                         db=config['database_name'])
    except:
        print("连接异常")
        return False
    return db


def version(db=""):
    """查看数据库版本号
        参数：
            db 数据库连接 由mysql_connect产生
    """
    # 打开数据库连接
    if db == "":
        db = mysql_connect()
    cursor = db.cursor()
    cursor.execute("select version()")
    return cursor.fetchone()


# 创建数据表
def create_datebase(db=""):
    """创建数据表
        参数：
            db 数据库连接 由mysql_connect产生
    """
    # 打开数据库连接
    if db == "":
        db = mysql_connect()
    # 获取操作游标
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS student_info")

    # 使用预处理语句创建表
    sql = """CREATE TABLE student_info (
             first_name  CHAR(20) NOT NULL,
             last_name  CHAR(20),
             age INT,  
             sex CHAR(1),
             class CHAR(20) )"""
    # 执行sql
    try:
        result = cursor.execute(sql)
    except:
        db.close()
        print("创建表失败")
        return False
    db.close()
    return True


def insert_info(db=""):
    """插入数据
        参数：
            db 数据库连接 由mysql_connect产生
    """
    if db == "":
        db = mysql_connect()
    cursor = db.cursor()
    num = 0
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
            num = num + 1
        except:
            # 如果发生错误则回滚并关闭数据库连接
            db.rollback()
            db.close()
            print(f'已插入{num}条数据。')
            return False
    # 关闭数据库连接
    db.close()
    print(f'已插入{num}条数据。')
    return True


def select_info(db=""):
    """查询数据
        参数：
            db 数据库连接 由mysql_connect产生
    """
    if db == "":
        db = mysql_connect()
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM student_info WHERE %s = '%s'" % ("class", "软件1181")
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # for row in results:
        #     fname = row[0]
        #     lname = row[1]
        #     age = row[2]
        #     sex = row[3]
        #     cla = row[4]
        #     # 打印结果
        #     print("first_name=%s,last_name=%s,age=%s,sex=%s,class=%s" % (fname, lname, age, sex, cla))
    except:
        print("Error: unable to fetch data")
        db.close()
        return False
    # 关闭数据库连接
    db.close()
    return results


def update_info(db=""):
    """更新数据"""
    if db == "":
        db = mysql_connect()
    cursor = db.cursor()
    # SQL 更新语句
    sql = "UPDATE student_info SET AGE = AGE + 1 WHERE SEX = '%c'" % 'f'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        print("执行sql出现错误！")
        return False
    # 关闭数据库连接
    db.close()
    return True


def delete_info(db=""):
    """删除信息"""
    if db == "":
        db = mysql_connect()
    cursor = db.cursor()
    # SQL 删除语句
    sql = "DELETE FROM  student_info WHERE AGE > %s" % (20)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        db.close()
        return False
    # 关闭连接
    db.close()
    return True

# insert_info()
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

if __name__ == "__main__":
    # print(create_datebase())
    # print(insert_info())
    # print("databse version:%s" % version())
    print(select_info())
    # print(update_info())
    # print(delete_info())

    # config = configparser.RawConfigParser()
    # config.read("config.txt")
    # secs = config.sections()
    # print(secs)
    # options = config.options("mysql")
    # print(options)
    # database_name = config.get("mysql","database_name")
    # print(database_name)
    # config = get_config.get_config('mysql')
    # print(config)

