from app.models.general import connect_to_sql


class CourseReader:
    def __init__(self):
        self.data = read_course()


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
