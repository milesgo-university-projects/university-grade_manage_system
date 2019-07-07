from wtforms import Form, StringField, IntegerField
from wtforms.validators import Regexp, Length, NumberRange


class AdminSelectSingleCourseForm(Form):
    # 课程编号为5位数字
    course_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='课程编号应为5位数字')])


class AdminUpdateCourseForm(Form):
    # 课程编号为5位数字
    course_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='课程编号应为5位数字')])
    # 课程名称长度小于20
    course_name = StringField(validators=[Length(min=0, max=20, message='课程名称过长')])
    # 开课年份为4为数字
    year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='开课年份应为4位数字')])
    # 专业取值为春、秋
    semester = StringField(validators=[Regexp(regex=r'^[春|秋]$', message='学期取值为春、秋')])
    # 教师编号为5位数字
    teacher_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])
    # 学分在1~10之间
    credit = IntegerField(validators=[NumberRange(min=1, max=10, message='学分应在1~10之间')])


class AdminInsertCourseForm(Form):
    # 课程名称长度小于20
    course_name = StringField(validators=[Length(min=0, max=20, message='课程名称过长')])
    # 开课年份为4为数字
    year = StringField(validators=[Regexp(regex=r'^[0-9]{4}$', message='开课年份应为4位数字')])
    # 专业取值为春、秋
    semester = StringField(validators=[Regexp(regex=r'^[春|秋]$', message='学期取值为春、秋')])
    # 教师编号为5位数字
    teacher_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])
    # 学分在1~10之间
    credit = IntegerField(validators=[NumberRange(min=1, max=10, message='学分应在1~10之间')])
