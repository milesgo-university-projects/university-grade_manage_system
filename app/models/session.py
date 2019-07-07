from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.models.general import connect_to_sql


class StudentPasswordChanger:
    def __init__(self, student_id, old_password, new_password):
        self.data = student_change_password(student_id, old_password, new_password)


class TeacherPasswordChanger:
    def __init__(self, teacher_id, old_password, new_password):
        self.data = teacher_change_password(teacher_id, old_password, new_password)


class LoginChecker(UserMixin):
    def __init__(self, function, role, tmp_id, password):
        if function == 'login':
            self.role = role
            self.id = role + tmp_id
            self.true_id = tmp_id
            self.password = password
            if role == 'student':
                self.data = student_login_check(tmp_id, password)
            elif role == 'teacher':
                pass
            elif role == 'admin':
                pass
            else:
                pass
        else:
            self.role = role
            self.id = role + tmp_id
            self.true_id = tmp_id

    def get_role(self):
        return self.role

    def get_true_id(self):
        return self.true_id


class StudentLoginChecker(UserMixin):
    def __init__(self, student_id, password):
        self.student_id = student_id
        self.data = student_login_check(student_id, password)

    def get_id(self):
        return 'student' + self.student_id


def student_login_check(student_id, password):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select password from student where student_id = \'%s\'; ' % student_id
            cursor.execute(sql)
            password_hash = cursor.fetchone()
            if password_hash is None:
                data['error'] = '学生不存在，请检查学生编号';
                return data
            password_hash = password_hash[0]
            if not check_password_hash(password_hash, password):
                data['error'] = '密码错误，登录失败'
                return data
            cursor.execute(sql)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


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
