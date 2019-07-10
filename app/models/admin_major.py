from app.models.general import connect_to_sql


class MajorIdReader:
    def __init__(self):
        self.data = read_major_id()


class MajorReader:
    def __init__(self):
        self.data = read_major()


class SingleMajorReader:
    def __init__(self, major_id):
        self.data = read_single_major(major_id)


class MajorUpdater:
    def __init__(self, major_id, major_name):
        self.data = update_major(major_id, major_name)


class MajorInserter:
    def __init__(self, major_name):
        self.data = insert_major(major_name)


class MajorDeleter:
    def __init__(self, major_id):
        self.data = delete_major(major_id)


def delete_major(major_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'delete from major where major_id = \'%s\';' % major_id
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def get_new_major_id():
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select max(convert(major_id, unsigned integer))+1 from major order by major_id'
            cursor.execute(sql)
            tmp = cursor.fetchone()[0]
            if tmp is None:
                data['major_id'] = '001'
            else:
                data['major_id'] = str(tmp)
                while len(data['major_id']) < 3:
                    data['major_id'] = '0' + data['major_id']
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


def insert_major(major_name):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            major_id = get_new_major_id()
            if major_id.get('error'):
                data['error'] = major_id['error']
                return data
            sql = 'insert into major values(\'%s\', \'%s\');' % (major_id['major_id'], major_name)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def update_major(major_id, major_name):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'update major set major_name = \'%s\' where major_id = \'%s\';' % (major_name, major_id)
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        data['error'] = str(e)
        connection.rollback()
    finally:
        connection.close()
    return data


def read_single_major(major_id):
    connection = connect_to_sql()
    data = {}
    try:
        with connection.cursor() as cursor:
            sql = 'select major_id, major_name from major where major_id = \'%s\';' % major_id
            cursor.execute(sql)
            result = cursor.fetchone()
            data['major_id'] = result[0]
            data['major_name'] = result[1]
    except Exception as e:
        data['error'] = str(e)
    finally:
        connection.close()
    return data


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
                  'group by m.major_id ' \
                  'order by m.major_id;'
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
