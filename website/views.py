from flask import Blueprint, render_template

test = {"email" : 'Krishna@gmail.com'}


views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    return render_template('home.html')