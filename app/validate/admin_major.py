from wtforms import Form, StringField
from wtforms.validators import Regexp, Length


class AdminSelectSingleMajorForm(Form):
    # 专业编号为3位数字
    major_id = StringField(validators=[Regexp(regex=r'^[0-9]{3}$', message='专业编号应为3位数字')])


class AdminUpdateMajorForm(Form):
    # 专业编号为3位数字
    major_id = StringField(validators=[Regexp(regex=r'^[0-9]{3}$', message='专业编号应为3位数字')])
    # 专业名称长度小于20
    major_name = StringField(validators=[Length(min=0, max=20, message='专业名称过长')])


class AdminInsertMajorForm(Form):
    # 专业名称长度小于20
    major_name = StringField(validators=[Length(min=0, max=20, message='专业名称过长')])