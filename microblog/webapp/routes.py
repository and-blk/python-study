from flask import render_template, redirect, url_for, flash, request
from webapp import app
from webapp.form import LoginForm
from webapp.dataprocessing import DataProcessing


SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']
hosts = ['localhost', 'localhost', 'localhost']
pwd = 'root'
usr = 'root'


@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", title='Home')


@app.route('/about')
def about():
    return render_template("about.html", title='about')


@app.route('/kernels', methods=['POST', 'GET'])
def kernels():
    ldata = []
    if request.method == 'POST':
        for host in hosts:
            vers = DataProcessing.remote_session(host, usr, pwd, ldata)
            DataProcessing.commit(host=host, vers=vers)
        return render_template('kernels.html', data=DataProcessing.fetch())
    return render_template("kernels.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('reqested access for {}'.format(form.username.data))
        return redirect(url_for("home"))
    return render_template('login.html', form=form, title='login')
