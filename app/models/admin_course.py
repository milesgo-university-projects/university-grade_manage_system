from app.models.general import connect_to_sql


class CourseReader:
    def __init__(self):
        self.data = read_course()


class SingleCourseReader:
    def __init__(self, course_id):
        self.data = read_single_course(course_id)


class CourseDeleter:
    def __init__(self, course_id):
        self.data = delete_course(course_id)


class CourseInserter:
    def __init__(self, course_name, year, semester, teacher_id, credit):
        self.data = insert_course(course_name, year, semester, teacher_id, credit)


class CourseUpdater:
    def __init__(self, course_id, course_name, year, semester, teacher_id, credit):
        self.data = update_course(course_id, course_name, year, semester, teacher_id, credit)


class CourseTeacherReader:
    def __init__(self, course_id):
        self.data = get_teacher_of_course(course_id)


def get_teacher_of_course(course_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select teacher_id from course where course_id = \'%s\';' % course_id
            cursor.execute(sql)
            result = cursor.fetchone()
            if result is None:
                data['error'] = '课程编号不存在'
                return data
            data['teacher_id'] = result[0]
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def update_course(course_id, course_name, year, semester, teacher_id, credit):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'update course set course_name = \'%s\', year = \'%s\', semester = \'%s\',' \
                  'teacher_id = \'%s\', credit = %d where course_id = \'%s\';' \
                  % (course_name, year, semester, teacher_id, credit, course_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def read_single_course(course_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select course_id, course_name, year, semester, teacher_id, credit ' \
                  'from course where course_id = \'%s\';' % course_id
            cursor.execute(sql)
            result = cursor.fetchone()
            data['course_id'] = result[0]
            data['course_name'] = result[1]
            data['year'] = result[2]
            data['semester'] = result[3]
            data['teacher_id'] = result[4]
            data['credit'] = result[5]
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def insert_course(course_name, year, semester, teacher_id, credit):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            course_id = get_new_course_id()
            if course_id.get('error'):
                data['error'] = course_id['error']
                return data
            sql = 'insert into course values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', %d);' \
                  % (course_id['course_id'], course_name, year, semester, teacher_id, credit)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def get_new_course_id():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select max(convert(course_id, unsigned integer))+1 from course order by course_id'
            cursor.execute(sql)
            tmp = cursor.fetchone()[0]
            if tmp is None:
                data['course_id'] = '00001'
            else:
                data['course_id'] = str(tmp)
                while len(data['course_id']) < 5:
                    data['course_id'] = '0' + data['course_id']
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def delete_course(course_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'delete from course where course_id = \'%s\'; ' % course_id
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_course():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select tmp.course_id, tmp.course_name, tmp.year, tmp.semester, tmp.teacher_id, ' \
                  'tmp.credit, tmp.number_of_students, tmp.average_grade, t.teacher_name from ( ' \
                  'select c.course_id, course_name, year, semester, teacher_id, credit, count(student_id), avg(grade) ' \
                  'from course as c left outer join student_course as sc ' \
                  'on c.course_id = sc.course_id ' \
                  'group by c.course_id ' \
                  ') as tmp(course_id, course_name, year, semester, teacher_id, ' \
                  'credit, number_of_students, average_grade), teacher as t ' \
                  'where tmp.teacher_id = t.teacher_id ' \
                  'order by tmp.course_id; '
            cursor.execute(sql)
            result = cursor.fetchall()
            data['courses'] = []
            for row in result:
                average_grade = row[7]
                if average_grade is None:
                    average_grade = 0
                tmp = {'course_id': row[0], 'course_name': row[1], 'year': row[2], 'semester': row[3],
                       'teacher_id': row[4], 'credit': row[5], 'number_of_students': row[6],
                       'average_grade': round(float(average_grade), 2), 'teacher_name': row[8]}
                data['courses'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
