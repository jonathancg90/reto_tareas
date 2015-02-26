from flask import render_template
from flask.ext.wtf import Form
from flask import redirect, url_for
from app import db
import time
import datetime
from threading import Thread
from wtforms.ext.sqlalchemy.orm import model_form
from app import app
from app import models

def print_queue_size():
    while True:
        tasks = models.Task.query.filter(models.Task.status != models.Task.STATUS_COMPLETE).all()
        for task in tasks:
            task.status = models.Task.STATUS_EXECUTE
            db.session.commit()
            app.logger.debug("Execute Task: %s" % (task.name))
            time.sleep(task.time)
            task.status = models.Task.STATUS_COMPLETE
            db.session.commit()
        time.sleep(1)

t = Thread(target=print_queue_size, args=())
t.setDaemon(True)
t.start()

@app.route('/')
@app.route('/index')
def index():
    tasks = models.Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/task/create', methods=['GET', 'POST'])
def task_create():
    my_form = model_form(models.Task, base_class=Form)
    form = my_form()
    if form.validate_on_submit():
        new_task = models.Task(
            name=form.name.data,
            time=form.time.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('task_list'))
    else:
        pass
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