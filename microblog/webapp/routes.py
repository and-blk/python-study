from flask import render_template, redirect, url_for, flash, request
from webapp import app
from webapp.form import LoginForm
from webapp.getvers import GetVersion


SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']
hosts = ['localhost', 'localhost']
pwd = 'root'
usr = 'root'



@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", title='Home')


@app.route('/about')
def about():
    return render_template("about.html", title='about')


@app.route('/today_kern', methods=['POST', 'GET'])
def today_kern():
    list_data = []
    if request.method == 'POST':
        #data = GetVersion.remote_cmd(hosts, usr, pwd)
        GetVersion.data_collection(hosts, usr, pwd, list_data)
        return render_template('result.html', data=list_data)
    return render_template("today_kern.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('reqested access for {}'.format(form.username.data))
        return redirect(url_for("home"))
    return render_template('login.html', form=form, title='login')
