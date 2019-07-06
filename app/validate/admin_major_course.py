from wtforms import Form, StringField
from wtforms.validators import Regexp


class AdminMajorCourseForm(Form):
    # 专业编号为3位数字
    major_id = StringField(validators=[Regexp(regex=r'^[0-9]{3}$', message='专业编号应为3位数字')])
    # 课程编号为5位数字
    course_id = StringField(validators=[Regexp(regex=r'^[0-9]{5}$', message='课程编号应为3位数字')])
