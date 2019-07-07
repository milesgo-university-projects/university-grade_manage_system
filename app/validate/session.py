from wtforms import Form, StringField
from wtforms.validators import Regexp


class StudentLoginForm(Form):
    student_id = StringField(validators=[Regexp(regex=r'^[0-9]{10}$', message='学生编号应为10位数字')])
    password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='密码应为5~18位数字或字母组成')])


class StudentChangePasswordForm(Form):
    # 学生编号为10位数字
    student_id = StringField(validators=[Regexp(regex=r'^[0-9]{10}$', message='学生编号应为10位数字')])
    old_password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='旧密码应为5~18位数字或字母组成')])
    new_password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='新密码应为5~18位数字或字母组成')])


class TeacherLoginForm(Form):
    teacher_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])
    password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='密码应为5~18位数字或字母组成')])


class AdminLoginForm(Form):
    password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='密码应为5~18位数字或字母组成')])


class TeacherChangePasswordForm(Form):
    # 教师编号为5位数字
    teacher_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])
    old_password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='旧密码应为5~18位数字或字母组成')])
    new_password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='新密码应为5~18位数字或字母组成')])


class AdminLoginForm(Form):
    password = StringField(validators=[Regexp(regex=r'^[0-9a-zA-Z]{5,18}$', message='旧密码应为5~18位数字或字母组成')])
