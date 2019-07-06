from flask import Blueprint

web = Blueprint('web', __package__)

from app.web import student
from app.web import teacher
from app.web import admin_student
from app.web import admin_teacher
from app.web import admin_course
from app.web import admin_major
from app.web import admin_major_course
from app.web import session