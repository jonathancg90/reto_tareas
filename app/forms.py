from flask.ext.wtf import Form
from wtforms import StringField


class TaskForm(Form):
    name = StringField('Nombre')
    time = StringField('Tiempo (Seg)')