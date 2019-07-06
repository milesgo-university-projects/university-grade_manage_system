import pymysql
from flask import current_app


def connect_to_sql():
    connection = pymysql.connect(host='localhost', user=current_app.config['DATABASE_USER'],
                                 password=current_app.config['DATABASE_PASSWORD'],
                                 database='grade_manage_system', charset='utf8')
    return connection
