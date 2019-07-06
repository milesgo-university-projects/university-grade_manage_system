from app.models.general import connect_to_sql


class TeacherReader:
    def __init__(self, teacher_id):
        self.data = read_base_information(teacher_id)
        if self.data.get('error'):
            return
        self.data = dict(self.data, **read_number_of_courses(teacher_id))


class TeacherCoursesReader:
    def __init__(self, teacher_id):
        self.data = read_selected_courses(teacher_id)


class TeacherCourseStudentReader:
    def __init__(self, course_id):
        self.data = read_selected_students(course_id)


class TeacherGradeUpdater:
    def __init__(self, course_id, student_id, grade):
        self.data = update_student_grade(course_id, student_id, grade)


class CourseStatisticReader:
    def __init__(self, course_id):
        self.data = read_course_statistic(course_id)


def read_base_information(teacher_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            # 查询教师基本信息
            sql = 'select teacher_id, teacher_name, sex, birth_year ' \
                  'from teacher ' \
                  'where teacher_id = %s;' % teacher_id
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                data['teacher_id'] = result[0]
                data['teacher_name'] = result[1]
                data['sex'] = result[2]
                data['birth_year'] = result[3]
            else:
                data['error'] = 'teacher id ' + teacher_id + ' not found in database'
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_number_of_courses(teacher_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            # 查询教师所授课程数量
            sql = 'select count(course_id) from course ' \
                  'where teacher_id = %s;' % teacher_id
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                data['number_of_courses'] = int(result[0])
            else:
                data['number_of_courses'] = 0
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_selected_courses(teacher_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            # 查询教师授课列表
            sql = 'select course_id, course_name, year, semester, credit ' \
                  'from course ' \
                  'where teacher_id = %s ' % teacher_id
            cursor.execute(sql)
            result = cursor.fetchall()
            data['courses'] = []
            if result:
                for row in result:
                    tmp = {'course_id': row[0], 'course_name': row[1], 'year': row[2], 'semester': row[3],
                           'credit': row[4]}
                    data['courses'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_selected_students(course_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            # 查询选课学生列表
            sql = 'select s.student_id, s.student_name, s.sex, m.major_name, sc.grade ' \
                  'from student_course as sc, student as s, major as m ' \
                  'where sc.student_id = s.student_id and s.major_id = m.major_id ' \
                  'and course_id = %s ' % course_id
            cursor.execute(sql)
            result = cursor.fetchall()
            data['students'] = []
            if result:
                for row in result:
                    tmp = {'student_id': row[0], 'student_name': row[1], 'sex': row[2], 'major_name': row[3],
                           'grade': row[4]}
                    data['students'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_course_statistic(course_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            # 查询某课程统计信息
            sql = 'select s.student_id, s.student_name, s.sex, m.major_name, sc.grade ' \
                  'from student_course as sc, student as s, major as m ' \
                  'where sc.student_id = s.student_id and s.major_id = m.major_id ' \
                  'and course_id = %s ' % course_id
            cursor.execute(sql)
            result = cursor.fetchall()
            data['students'] = []
            if result:
                for row in result:
                    tmp = {'student_id': row[0], 'student_name': row[1], 'sex': row[2], 'major_name': row[3],
                           'grade': row[4]}
                    data['students'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def update_student_grade(course_id, student_id, grade):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            # 更新学生某课程成绩
            sql = 'update student_course ' \
                  'set grade = %s ' \
                  'where course_id = %s and student_id = %s;' % (grade, course_id, student_id)
            result = cursor.execute(sql)
            if result != 1:
                data['error'] = 'update student_course table error'
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
