from app.models.general import connect_to_sql
from app.models.student import StudentReader
from werkzeug.security import generate_password_hash


class StudentListReader:
    def __init__(self):
        data = read_student_id_list()
        if data.get('error'):
            return
        student_id_list = data['student_id']
        self.data = {'students': []}
        for student_id in student_id_list:
            tmp = StudentReader(student_id)
            if tmp.data.get('error'):
                self.data['error'] = tmp.data['error']
                return
            self.data['students'].append(tmp.data)


class StudentUpdater:
    def __init__(self, student_id, student_name, sex, birth_year, province, enter_year, major_id):
        self.data = update_student(student_id, student_name, sex, birth_year, province, enter_year, major_id)


class StudentInserter:
    def __init__(self, student_name, sex, birth_year, province, enter_year, major_id):
        self.data = insert_student(student_name, sex, birth_year, province, enter_year, major_id)


class StudentDeleter:
    def __init__(self, student_id):
        self.data = delete_student(student_id)


def delete_student(student_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'delete from student where student_id = \'%s\'; ' % student_id
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def insert_student(student_name, sex, birth_year, province, enter_year, major_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            student_id = get_new_student_id(enter_year, major_id)
            password = generate_password_hash(student_id['student_id'])
            sql = 'insert into student values ' \
                  '(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\'); ' \
                  % (student_id['student_id'], student_name, sex, birth_year, province, enter_year, major_id, password)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def update_student(student_id, student_name, sex, birth_year, province, enter_year, major_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'update student set student_name = \'%s\', sex = \'%s\', birth_year = \'%s\', ' \
                  'province = \'%s\', enter_year = \'%s\', major_id = \'%s\' where student_id = \'%s\'; ' % \
                  (student_name, sex, birth_year, province, enter_year, major_id, student_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def read_student_id_list():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select student_id from student order by student_id;'
            cursor.execute(sql)
            data['student_id'] = cursor.fetchall()
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def get_new_student_id(enter_year, major_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select max(convert(right(student_id, 3), unsigned integer))+1 from student ' \
                  'where enter_year = \'%s\' and major_id = \'%s\' order by student_id;' % (enter_year, major_id)
            cursor.execute(sql)
            tmp = cursor.fetchone()[0]
            if tmp is None:
                data['student_id'] = enter_year + major_id + '001'
            else:
                part_id = str(tmp)
                while len(part_id) < 3:
                    part_id = '0' + part_id
                data['student_id'] = enter_year + major_id + part_id
                print(data['student_id'])
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
