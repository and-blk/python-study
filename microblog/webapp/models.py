from webapp import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

#Hey there this is my file
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#This is another test message for test branch
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(164))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Kernel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow())
    server_name = db.Column(db.String(20))

    def __repr__(self):
        return '<Kernel {}>'.format(self.version)
