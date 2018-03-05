from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
app.debug = True
#设置WTF key
app.config['SECRET_KEY'] = 'hello quanqin.org'


from app.Views import home_view
from app import Views

bootstrap = Bootstrap(app)
app.register_blueprint(home_view)
login_manger = LoginManager()
login_manger.init_app(app)

# 404 page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
