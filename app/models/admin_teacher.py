from werkzeug.security import generate_password_hash

from app.models.general import connect_to_sql


class TeacherListReader:
    def __init__(self):
        self.data = read_teacher_list()


class TeacherIdReader:
    def __init__(self):
        self.data = read_teacher_id()


class TeacherUpdater:
    def __init__(self, teacher_id, teacher_name, sex, birth_year):
        self.data = update_teacher(teacher_id, teacher_name, sex, birth_year)


class TeacherInserter:
    def __init__(self, teacher_name, sex, birth_year):
        self.data = insert_teacher(teacher_name, sex, birth_year)


class TeacherDeleter:
    def __init__(self, teacher_id):
        self.data = delete_teacher(teacher_id)


def read_teacher_id():
    connection = connect_to_sql()
    data = {'teacher_ids': []}
    try:
        with connection.cursor() as cursor:
            sql = 'select teacher_id from teacher'
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                data['teacher_ids'].append(row[0])
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def delete_teacher(teacher_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'delete from teacher where teacher_id = \'%s\'; ' % teacher_id
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def get_new_teacher_id():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select max(convert(teacher_id, unsigned integer))+1 from teacher order by teacher_id'
            cursor.execute(sql)
            tmp = cursor.fetchone()[0]
            if tmp is None:
                data['teacher_id'] = '00001'
            else:
                data['teacher_id'] = str(tmp)
                while len(data['teacher_id']) < 5:
                    data['teacher_id'] = '0' + data['teacher_id']
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def insert_teacher(teacher_name, sex, birth_year):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            teacher_id = get_new_teacher_id()
            password = generate_password_hash(teacher_id['teacher_id'])
            if teacher_id.get('error'):
                data['error'] = teacher_id['error']
                return data
            sql = 'insert into teacher values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' \
                  % (teacher_id['teacher_id'], teacher_name, sex, birth_year, password)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def update_teacher(teacher_id, teacher_name, sex, birth_year):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'update teacher set teacher_name = \'%s\', sex = \'%s\', birth_year = \'%s\' ' \
                  'where teacher_id = \'%s\'; ' % \
                  (teacher_name, sex, birth_year, teacher_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def read_teacher_list():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select t.teacher_id, teacher_name, sex, birth_year, count(course_id) as number_of_courses ' \
                  'from teacher as t left outer join course as c ' \
                  'on c.teacher_id = t.teacher_id ' \
                  'group by t.teacher_id ' \
                  'order by t.teacher_id;'
            cursor.execute(sql)
            result = cursor.fetchall()
            data['teachers'] = []
            for row in result:
                tmp = {'teacher_id': row[0], 'teacher_name': row[1], 'sex': row[2],
                       'birth_year': row[3], 'number_of_courses': row[4]}
                data['teachers'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
