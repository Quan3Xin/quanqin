from flask import render_template, request, flash, session, redirect, url_for
from . import home_view
from app.models.model import User
from app import app
from app.control import forms
from app.models.model import db

import json

from bs4 import BeautifulSoup
import urllib
import traceback


class city_link(object):
    name = ""
    link = ""

    def __init__(self, name, link):
        self.name = name
        self.link = link


@home_view.route('/')
@home_view.route('/index')
def index():
    URL = 'http://www.amis.pk/DistrictCities.aspx'

    return render_template("index.html",
                           title='Home')


@app.route('/new/<data>', methods=['GET', 'POST'])
def new(data):
    return render_template("new.html",
                           title='Home',
                           link=data)


@home_view.route('/login', methods=['GET', 'POST'])
def log():
    # waring 参考第八章
    error = None
    form_table = forms.Name_Form()
    if form_table.validate_on_submit():
        data = form_table.data
        admin = User.query.filter_by(name=form_table.data['name']).first()
        # pwd = User.query.filter_by(pwd=data['password']).first()

        print(admin)
        if admin != None:
            if admin.verify_password(data['password']):
                print('===============================<>')
                return redirect(url_for('home_view.error'))
            else:
                print(admin)
                print('<------------------------->')
                session['kown'] = True
                data = ''
                return redirect(request.args.get('next') or url_for('home_view.index'))
    return render_template('login.html', error=error, form=form_table)

@home_view.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    forms_register = forms.Register_Form()
    if forms_register.validate_on_submit():
        user = User(name = forms_register.name.data, pwd=forms_register.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(request.args.get('next') or url_for('home_view.index'))
    return render_template('register.html', form=forms_register, error=error)
@home_view.route('/error')
def error():
    return render_template('error.html')


"""
 flash('account Invalid')
 print(admin, '+++++')
 return redirect(url_for('home_view.log'))
if not admin.check_pwd(pwd=int(data['pwd'])):
 flash("Invalid password")
 return redirect(url_for('home_view.log'))
session['admin'] = data['account']
return redirect(request.args.get('next') or url_for('home_view.index'))
"""
