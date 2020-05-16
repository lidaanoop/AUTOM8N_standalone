import os

from flask import Flask, render_template, request, redirect, session, url_for
from simplepam import authenticate

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
    username=session.get('username')
    return render_template("domain-form.html", username=username)


@app.route('/adddomain', methods=['GET', 'POST'])
def adddomain():
    username = session.get('username')
    return render_template('home.html',username=username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=None, debug=True)
