import pymysql


def connect_to_sql():
    connection = pymysql.connect(host='localhost', user='root', password='137891zH',
                                 database='grade_manage_system', charset='utf8')
    return connection
