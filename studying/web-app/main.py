from flask import Flask, render_template, request, url_for, redirect, make_response, abort, session

app = Flask(__name__)
app.secret_key = 'fsdksdlflk43kj5r3llf'
#data = session['username']

req_name = str()
req_sur = str()


@app.route("/")
def index():
    if 'username' in session and 'surname' in session:
        #return "<p>You are logged in as %s</p>" % session['username']
        return render_template('home.html')
    return render_template("nlog.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        req_name = request.form['username']
        req_sur = request.form['usersurname']
        session['username'] = req_name
        session['surname'] = req_sur
        #resp = make_response(render_template('login.html'))
        #resp.set_cookie(username, username)
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template('out.html')


if __name__ == "__main__":
    app.run(debug=True)
