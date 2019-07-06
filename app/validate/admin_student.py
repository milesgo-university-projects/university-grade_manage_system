from wtforms import Form, StringField
from wtforms.validators import Regexp, Length


class UpdateStudentInformationForm(Form):
    # 学生编号为10位数字
    student_id = StringField(validators=[Regexp(regex=r'^[0-9]{10}$', message='学生编号应为10位数字')])
    # 学生姓名长度小于20
    student_name = StringField(validators=[Length(min=0, max=20, message='学生姓名过长')])
    # 性别取值为男、女
    sex = StringField(validators=[Regexp(regex=r'^[男|女]$', message='性别取值为男、女')])
    # 出生年份为4为数字
    birth_year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='出生年份应为4位数字')])
    # 省份名称长度小于20
    province = StringField(validators=[Length(min=0, max=20, message='省份名称过长')])
    # 入学年份为4为数字
    enter_year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='入学年份应为4位数字')])
    # 专业编号为3位数字
    major_id = StringField(validators=[Regexp(regex=r'^[0-9]{3}$', message='专业编号应为3位数字')])


class InsertStudentInformationForm(Form):
    # 学生姓名长度小于20
    student_name = StringField(validators=[Length(min=0, max=20, message='学生姓名过长')])
    # 性别取值为男、女
    sex = StringField(validators=[Regexp(regex=r'^[男|女]$', message='性别取值为男、女')])
    # 出生年份为4为数字
    birth_year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='出生年份应为4位数字')])
    # 省份名称长度小于20
    province = StringField(validators=[Length(min=0, max=20, message='省份名称过长')])
    # 入学年份为4为数字
    enter_year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='入学年份应为4位数字')])
    # 专业编号为3位数字
    major_id = StringField(validators=[Regexp(regex=r'^[0-9]{3}$', message='专业编号应为3位数字')])
