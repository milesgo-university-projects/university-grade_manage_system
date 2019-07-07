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
            data['course_id'] = str(cursor.fetchone()[0])
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
            sql = 'select c.course_id, course_name, year, semester, teacher_id, credit, ' \
                  'count(student_id) as number_of_students, avg(grade) as average_grade ' \
                  'from course as c left outer join student_course as sc ' \
                  'on c.course_id = sc.course_id ' \
                  'group by c.course_id;'
            cursor.execute(sql)
            result = cursor.fetchall()
            data['courses'] = []
            for row in result:
                tmp = {'course_id': row[0], 'course_name': row[1], 'year': row[2], 'semester': row[3],
                       'teacher_id': row[4], 'credit': row[5], 'number_of_students': row[6], 'average_grade': float(row[7])}
                data['courses'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
