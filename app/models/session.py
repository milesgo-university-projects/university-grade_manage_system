from werkzeug.security import generate_password_hash, check_password_hash

from app.models.general import connect_to_sql


class StudentPasswordChanger:
    def __init__(self, student_id, old_password, new_password):
        self.data = student_change_password(student_id, old_password, new_password)


class TeacherPasswordChanger:
    def __init__(self, teacher_id, old_password, new_password):
        self.data = teacher_change_password(teacher_id, old_password, new_password)


def teacher_change_password(teacher_id, old_password, new_password):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select password from teacher where teacher_id = \'%s\'; ' % teacher_id
            cursor.execute(sql)
            password_hash = cursor.fetchone()[0]
            if not check_password_hash(password_hash, old_password):
                data['error'] = '旧密码错误，修改密码失败'
                return data
            sql = 'update teacher set password = \'%s\' where teacher_id = \'%s\'; ' \
                  % (generate_password_hash(new_password), teacher_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def student_change_password(student_id, old_password, new_password):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select password from student where student_id = \'%s\'; ' % student_id
            cursor.execute(sql)
            password_hash = cursor.fetchone()[0]
            if not check_password_hash(password_hash, old_password):
                data['error'] = '旧密码错误，修改密码失败'
                return data
            sql = 'update student set password = \'%s\' where student_id = \'%s\'; ' \
                  % (generate_password_hash(new_password), student_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
