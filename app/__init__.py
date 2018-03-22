from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:c3@176.122.167.111/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
#设置WTF key
app.config['SECRET_KEY'] = 'hello quanqin.org'


from app.Views import home_view
from app import Views

bootstrap = Bootstrap(app)
app.register_blueprint(home_view)
"""login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home_view.log'
login_manager.session_protection = 'None'
login_manager.login_message = u"Bonvolu ensaluti por uzi tio pa臐o."
"""

def create_app(config_name):
    pass

# 404 page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
