from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

@auth.route('/login')
def home():
    return "<h>I am login Page</h>"