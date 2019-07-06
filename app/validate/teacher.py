from wtforms import Form, StringField, IntegerField
from wtforms.validators import Regexp, NumberRange


class GetTeacherInformationForm(Form):
    # 教师编号为5位数字
    teacher_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])


class GetCourseInformationForm(Form):
    # 课程编号为5位数字
    course_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='教师编号应为5位数字')])


class PostGradeInformationForm(Form):
    # 课程编号为5位数字
    course_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='课程编号应为5位数字')])
    # 学生编号为10位数字
    student_id = StringField(validators=[Regexp(regex=r'^[0-9]{10}$', message='学生编号应为10位数字')])
    # grade为0~100
    grade = IntegerField(validators=[NumberRange(min=0, max=100)])
