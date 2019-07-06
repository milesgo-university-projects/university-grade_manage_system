from app.models.general import connect_to_sql
from app.models.student import StudentReader


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
    def __init__(self, student_id, student_name, sex, birth_year, province, major_id):
        self.data = update_student(student_id, student_name, sex, birth_year, province, major_id)


def update_student(student_id, student_name, sex, birth_year, province, major_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'update student set student_name = \'%s\', sex = \'%s\', birth_year = \'%s\', ' \
                  'province = \'%s\', major_id = \'%s\' where student_id = \'%s\'; ' % \
                  (student_name, sex, birth_year, province, major_id, student_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_student_id_list():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select student_id from student'
            cursor.execute(sql)
            data['student_id'] = cursor.fetchall()
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
