#coding:utf8
from flask import Flask
#: from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
from app import app

if __name__ == '__main__':
    app.run(port=8391, debug=True)