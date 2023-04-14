import pymysql

from test.database_model.read_config import ReadConfig

class MysqlConnect:
    def __init__(self):
        self.host = ReadConfig().read_config("DATABASE", "host")
        self.port = eval(ReadConfig().read_config("DATABASE", "port"))
        self.username = ReadConfig().read_config("DATABASE", "username")
        self.password = ReadConfig().read_config("DATABASE", "password")
        self.data_base = ReadConfig().read_config("DATABASE", "data_base")

    # 连接数据库查询
    def connect_db_search(self, sql):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password,
                               db=self.data_base)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        search_msg = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return search_msg

    # 连接数据库更新
    def connect_db_update(self, sql):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password,
                               db=self.data_base)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        update_msg = cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return update_msg

    # 连接数据库新增
    def connect_db_insert(self, sql):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password,
                               db=self.data_base)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        insert_msg = cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return insert_msg

    # 连接数据库删除
    def connect_db_delete(self, sql):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password,
                               db=self.data_base)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        delete_msg = cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return delete_msg


if __name__ == '__main__':
    # sql1 = "select * from citms_device ;"
    # search_msg = MysqlConnect().connect_db_insert(sql1)
    # print(search_msg)

    # sql2 = "update test1 set name='222' where id > 2;"
    # update_msg = MysqlConnect().connect_db_update(sql2)
    # print(update_msg)
    #
    sql3 = "insert into sys_user_role  values(99,2);"
    insert_msg = MysqlConnect().connect_db_insert(sql3)
    print(insert_msg)
    #
    # sql4 = "delete from test1 where name='111'"
    # delete_msg = MysqlConnect().connect_db_insert(sql3)
    # print(delete_msg)
