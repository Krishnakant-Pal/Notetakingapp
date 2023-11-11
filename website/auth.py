from flask import Blueprint, render_template,request,flash,redirect,url_for
from flask_login import login_required,login_user, logout_user,current_user
from website.models import User
from website.config import db
auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(email)
        existing_user = user.find_user(email)

        if not existing_user:
        # if not user.find_user(email):
            flash('Please Signup first ', category='error')
            return redirect(url_for('auth.signup'))

        elif user.check_password( password):
            
            flash('You are logged in', category='success')
            login_user(user,remember=True)
            return redirect(url_for('views.home'))
        else: 
            flash('Incorrect password', category='error')
            return redirect(url_for('auth.login'))
    
    return render_template("login.html",user = current_user)



@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # user = User.query.filter_by(email=email).first()
        
        existing_user = db.user.find_one(email)

        if existing_user:
            flash('Email already exists.', category='error')
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:

            new_user = {
                "email": email,
                "username": first_name,
                "password": password1
            }
            user = User(email)
            user.create_user(**new_user)
            flash('Account created!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("signup.html",user= current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out', category='success')
    return redirect(url_for('auth.login'))