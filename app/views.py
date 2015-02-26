from flask import render_template
from flask.ext.wtf import Form
from flask import redirect, url_for
from app import db
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form
from app import app
from app import models

@app.route('/')
@app.route('/index')
def index():
    tasks = models.Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/task/create', methods=['GET', 'POST'])
def task_create():
    MyForm = model_form(models.Task, base_class=Form, field_args = {
        'name' : {
            'validators' : [validators.required]
        },
        'time' : {
            'validators' : [validators.required]
        }
    })
    form = MyForm()
    if form.validate_on_submit():
        new_task = models.Task(
            name=form.name.data,
            time=form.time.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('task_list'))
    return render_template('task/create.html', form=form)

@app.route('/task/delete/<pk>')
def task_delete(pk):
    task = models.Task.query.get(pk)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task_list'))

@app.route('/task')
def task_list():
    tasks = models.Task.query.all()
    return render_template('task/list.html', tasks=tasks)