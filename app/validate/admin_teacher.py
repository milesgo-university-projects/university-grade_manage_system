from wtforms import Form, StringField
from wtforms.validators import Regexp, Length


class AdminSelectSingleTeacherForm(Form):
    # 教师编号为5位数字
    teacher_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])


class AdminUpdateTeacherForm(Form):
    # 教师编号为5位数字
    teacher_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])
    # 教师姓名长度小于20
    teacher_name = StringField(validators=[Length(min=0, max=20, message='学生姓名过长')])
    # 性别取值为男、女
    sex = StringField(validators=[Regexp(regex=r'^[男|女]$', message='性别取值为男、女')])
    # 出生年份为4为数字
    birth_year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='出生年份应为4位数字')])


class AdminInsertTeacherForm(Form):
    # 教师姓名长度小于20
    teacher_name = StringField(validators=[Length(min=0, max=20, message='学生姓名过长')])
    # 性别取值为男、女
    sex = StringField(validators=[Regexp(regex=r'^[男|女]$', message='性别取值为男、女')])
    # 出生年份为4为数字
    birth_year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='出生年份应为4位数字')])
