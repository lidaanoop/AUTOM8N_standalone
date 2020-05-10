from flask import Flask, render_template, request, redirect, session
from simplepam import authenticate

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(str(username), str(password)):
            username = request.form['username']
            print(username)
            return render_template("home.html", username=username)
        else:
            return 'Invalid username/password'

    return redirect('index')


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
