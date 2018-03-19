# condig: utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from _datetime import datetime
from flask_login import  UserMixin
from app import db
from flask_login import login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)

    phone = db.Column(db.Integer, unique=True)

    info = db.Column(db.Text())

    face = db.Column(db.String(255), unique=True)
    uuid = db.Column(db.String(255), unique=True)
    # add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):

        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.pwd, password)

    def __repr__(self):
        return "<User %r>" % self.name

    def update(self):
        db.session.commit()
        return self

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)

    def load_user(user_id):
        return User.query.get(int(user_id))
class Pass_word(db.Model):
    __tablename__ = 'password'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)

    phone = db.Column(db.Integer, unique=True)

    info = db.Column(db.Text)

    face = db.Column(db.String(255), unique=True)
    uuid = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return "<Pass_world %r>" % self.id


class Pwd(db.Model):
    __tablename__ = 'pwd'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)

    phone = db.Column(db.Integer, unique=True)

    info = db.Column(db.Text)

    face = db.Column(db.String(255), unique=True)
    uuid = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<User %r>" % self.name

    def update(self):
        db.session.commit()
        return self


def add_data():
    data = User(name='12',
                pwd='22')
    db.session.add(data)
    db.session.commit()
