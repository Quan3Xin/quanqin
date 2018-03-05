from flask import Blueprint

home_view = Blueprint('home_view', __name__)

from app.Views import view
