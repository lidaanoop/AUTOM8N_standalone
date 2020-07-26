import os
import subprocess
import time
from celery import Celery
from flask import Flask, render_template, request, redirect, session, url_for
import celery.events.state
from requests import get
from simplepam import authenticate
from autom8ntaskq import displaycelery
from celery.result import AsyncResult
from celery.result import ResultBase

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    if 'username' in session:
        print(session['username'])

        return render_template("home.html")
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(str(username), str(password)):
            username = request.form['username']
            session['username'] = username
            print(session['username'])
            return render_template("home.html", username=username)
        else:
            return redirect('/')

    return redirect('index')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/domainform')
def domainform():
    username = session.get('username')
    return render_template("domain-form.html", username=username)


@app.route('/execute_action', methods=['GET', 'POST'])
def execute_action():
    global username, username1, domainname
    if request.method == 'POST':
        execute = request.form['execute']
        print(execute)
        if execute == 'adddomain':
            username = session.get('username')
            username1 = request.form['username']
            print(username1)
            password = request.form['password']
            print(password)
            domainname = request.form['domainname']
            print(domainname)
            results = displaycelery.delay()
            print(results.task_id)
            print(results.status)
            return render_template('execute_action.html', username=username, dict=dict, execute=execute,
                                   username1=username1, domainname=domainname, password=password)


@app.route('/listAllDomains', methods=['GET', 'POST'])
def listAllDomains():
    username = session.get('username')

    return render_template("listdomain.html", username=username, dict=dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=None, debug=True)
