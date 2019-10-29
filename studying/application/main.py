from flask import Flask, request, render_template, redirect, flash, url_for
from config import Config
from form import LoginForm




app = Flask(__name__)

app.config.from_object(Config)
SECRET_KEY = app.config['SECRET_KEY']



@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", title='Home')


@app.route('/about')
def about():
    return render_template("about.html", title='about')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('reqested access for {}'.format(form.username.data))
        return redirect(url_for("home"))
    return render_template('login.html', form=form, title='login')


if __name__ == "__main__":
    app.run(debug=True)
