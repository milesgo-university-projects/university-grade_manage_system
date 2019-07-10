from app.models.general import connect_to_sql


class StudentReader:
    def __init__(self, student_id):
        self.data = read_base_information(student_id)
        if self.data.get('error'):
            return
        self.data = dict(self.data, **read_total_credits(student_id))
        if self.data.get('error'):
            return
        self.data = dict(self.data, **read_number_of_courses(student_id))
        if self.data.get('error'):
            return
        self.data = dict(self.data, **read_average_grade(student_id))


class StudentCoursesReader:
    def __init__(self, student_id):
        self.data = read_selected_courses(student_id)


def read_base_information(student_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            # 查询学生基本信息
            sql = 'select student_id, student_name, sex, birth_year, province, enter_year, major_name, s.major_id ' \
                  'from student as s, major as m ' \
                  'where s.student_id = %s and s.major_id = m.major_id;' % student_id
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                data['student_id'] = result[0]
                data['student_name'] = result[1]
                data['sex'] = result[2]
                data['birth_year'] = result[3]
                data['province'] = result[4]
                data['enter_year'] = result[5]
                data['major_name'] = result[6]
                data['major_id'] = result[7]
            else:
                data['error'] = 'student id ' + student_id + ' not found in database'
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_total_credits(student_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select if(sum(credit) is null, 0, sum(credit)) from student as s, course as c, student_course as sc ' \
                  'where s.student_id = %s and s.student_id = sc.student_id ' \
                  'and c.course_id = sc.course_id and grade >= 60;' % student_id
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                data['credits'] = int(result[0])
            else:
                data['credits'] = 0
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_number_of_courses(student_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select count(course_id) from student_course ' \
                  'where student_id = %s;' % student_id
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


def read_average_grade(student_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select credit, grade from student_course as sc, course as c ' \
                  'where sc.student_id = %s and sc.course_id = c.course_id ' \
                  'and grade is not null;' % student_id
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                total_credit = 0
                total_grade = 0
                for row in result:
                    total_credit += row[0]
                    total_grade += row[0] * row[1]
                data['average_grade'] = round(float(1.0*total_grade/total_credit), 2)
            else:
                data['average_grade'] = 0
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_selected_courses(student_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select c.course_id, c.course_name, c.year, c.semester, t.teacher_name, c.credit, sc.grade ' \
                  'from course as c, student_course as sc, teacher as t ' \
                  'where sc.student_id = %s and sc.course_id = c.course_id ' \
                  'and t.teacher_id = c.teacher_id;' % student_id
            cursor.execute(sql)
            result = cursor.fetchall()
            data['courses'] = []
            for row in result:
                tmp = {'course_id': row[0], 'course_name': row[1], 'year': row[2], 'semester': row[3],
                       'teacher_name': row[4], 'credit': row[5], 'grade': row[6]}
                data['courses'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
