from flask import render_template, request, flash, session, redirect, url_for
from . import home_view
from app.models.model import User
from app import app
from functools import wraps
from app.control import forms
from app.models.model import db
from werkzeug.security import generate_password_hash
from flask_login import login_required
import json

from bs4 import BeautifulSoup

seesion = {}
seesion['user'] = 'userlogin'


def login_req(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('home_view.log', next=request.url))
        return func(*args, **kwargs)
    return decorated_function


@home_view.route('/')
@home_view.route('/index')
@login_req
def index():
    URL = 'http://www.amis.pk/DistrictCities.aspx'

    return render_template("index.html",
                           title='Home')


@home_view.route('/login', methods=['GET', 'POST'])
def log():
    # waring 参考第八章
    error = None
    form_table = forms.Name_Form()
    if form_table.validate_on_submit():
        data = form_table.data
        admin = User.query.filter_by(name=form_table.data['name']).first()
        # pwd = User.query.filter_by(pwd=data['password']).first()

        print(admin.check_pwd)
        if admin != None:
            if not admin.check_pwd(data['password']):
                print('===============================<>')
                print(admin.verify_password(data['password']))
                flash("密码or账号错误")
                return redirect(url_for('home_view.log'))
            else:
                print(admin)
                print('<------------------------->')
                session['admin'] = data['name']
                return redirect(request.args.get('next') or url_for('home_view.index'))

    return render_template('login.html', error=error, form=form_table)


@home_view.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    forms_register = forms.Register_Form()
    if forms_register.validate_on_submit():
        user = User(name=forms_register.name.data, pwd=generate_password_hash(forms_register.password.data))
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        print('-----------------------<>')
        return redirect(request.args.get('next') or url_for('home_view.index'))
    return render_template('register.html', form=forms_register, error=error)


@home_view.route('/error')
def error():
    return render_template('error.html')
