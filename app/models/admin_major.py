from app.models.general import connect_to_sql


class MajorIdReader:
    def __init__(self):
        self.data = read_major_id()


class MajorReader:
    def __init__(self):
        self.data = read_major()


def read_major_id():
    connection = connect_to_sql()
    data = {'major_ids': []}
    try:
        with connection.cursor() as cursor:
            sql = 'select major_id from major'
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                data['major_ids'].append(row[0])
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def read_major():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select m.major_id, major_name, count(student_id) as number_of_students ' \
                  'from major as m left outer join student as s ' \
                  'on m.major_id = s.major_id ' \
                  'group by m.major_id;'
            cursor.execute(sql)
            result = cursor.fetchall()
            data['majors'] = []
            for row in result:
                tmp = {'major_id': row[0], 'major_name': row[1], 'number_of_students': row[2]}
                data['majors'].append(tmp)
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data
