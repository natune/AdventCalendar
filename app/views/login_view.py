from flask import Blueprint, render_template

login_page = Blueprint('login', __name__)


@login_page.route('/login')
def login():
    return render_template('login.html')
