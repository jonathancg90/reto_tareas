from flask import render_template
from flask.ext.wtf import Form
# from wtforms.ext.appengine.db import model_form
from wtforms.ext.sqlalchemy.orm import model_form
from app import app
from app import models

@app.route('/')
@app.route('/index')
def index():
    tasks = models.Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/task/create')
def task_create():
    MyForm = model_form(models.Task, base_class=Form)
    form = MyForm()
    return render_template('task/create.html', form=form)

@app.route('/task/delete/<pk>')
def task_delete():
    return render_template('task/list.html')

@app.route('/task')
def task_list():
    tasks = models.Task.query.all()
    return render_template('task/list.html', tasks=tasks)