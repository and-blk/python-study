from flask import Flask, render_template, request, url_for, redirect, make_response, abort

app = Flask(__name__)

data = {"var1": "val1", "var2": "val2", "var3": "val3"}


@app.route("/")
def result():
    return render_template('home.html')


@app.route("/setcookie", methods = ["POST"])
def success():
    if request.method == "POST":
        user = request.form['username']
        surname = request.form['usersurname']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('IDuser', user, surname)

        return resp


@app.route("/getcookie")
def getcookie():
    return request.cookies.get('IDuser')


if __name__ == "__main__":
    app.run(debug=True)
