from flask_login import current_user


def check_authority(role, tmp_id):
    data = {}
    if current_user.get_role() == 'admin' and role == 'admin':
        return data
    if role != current_user.get_role() or tmp_id != current_user.get_true_id():
        data['error'] = '非法访问'
        data['current_user_role'] = current_user.get_role()
        data['current_user_id'] = current_user.get_true_id()
        data['request_user_role'] = role
        data['request_user_id'] = tmp_id
    return data

