from app.models.general import connect_to_sql
from app.models.admin_major import read_major
from app.models.admin_course import read_course


class MajorCourseReader:
    def __init__(self):
        self.data = read_major_course()


class InsertMajorCourseReader:
    def __init__(self):
        self.data = read_major()
        if self.data.get('error'):
            return
        self.data = dict(self.data, **read_course())


class MajorCourseInserter:
    def __init__(self, major_id, course_id):
        self.data = insert_major_course(major_id, course_id)


class MajorCourseDeleter:
    def __init__(self, major_id, course_id):
        self.data = delete_major_course(major_id, course_id)


def insert_major_course(major_id, course_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'insert into major_course values(\'%s\', \'%s\');' % (major_id, course_id)
            cursor.execute(sql)
            """
            sql = 'insert into student_course ( select student_id, \'%s\', ' \
                  'null from student where major_id = \'%s\');' % (course_id, major_id)
            cursor.execute(sql)
            """
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def delete_major_course(major_id, course_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            """
            sql = 'delete from student_course ' \
                  'where student_id in ( ' \
                      'select student_id ' \
                      'from student ' \
                      'where major_id = \'%s\') ' \
                  'and course_id = \'%s\'; ' % (major_id, course_id)
            cursor.execute(sql)
            """
            sql = 'delete from major_course ' \
                  'where major_id = \'%s\' and course_id = \'%s\' ' % (major_id, course_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def read_major_course():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select m.major_id, major_name, c.course_id, course_name ' \
                  'from major_course as mc, major as m, course as c ' \
                  'where mc.major_id = m.major_id and mc.course_id = c.course_id ' \
                  'order by m.major_id, c.course_id;'
            cursor.execute(sql)
            result = cursor.fetchall()
            data['major_courses'] = []
            for row in result:
                tmp = {'major_id': row[0], 'major_name': row[1], 'course_id': row[2], 'course_name': row[3]}
                data['major_courses'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
