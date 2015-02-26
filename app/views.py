from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/task/create')
def task_create():
    return render_template('index.html')

@app.route('/task/delete/<pk>')
def task_delete():
    return render_template('index.html')

@app.route('/task')
def task_list():
    return render_template('index.html')