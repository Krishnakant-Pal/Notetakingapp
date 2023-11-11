from flask import Blueprint, render_template,request,flash,redirect,url_for
from website.models import User
from website.config import db
auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User()
        existing_user = user.find_user(email)

        if not existing_user:
            flash('Please Signup first ', category='error')
            return redirect(url_for('auth.signup'))

        elif user.check_password(existing_user['password'], password):
            flash('You are logged in', category='success')
            return redirect(url_for('auth.home'))
        else: 
            flash('Incorrect password', category='error')
            return redirect(url_for('view.home'))
    
    return render_template("login.html")



@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # user = User.query.filter_by(email=email).first()
        user = User()
        existing_user = user.find_user(email)

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
            # new_user = [email=email,first_name=first_name,password=password1]
            new_user = {
                "email": email,
                "username": first_name,
                "password": password1
            }
            user.create_user(**new_user)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html")

@auth.route('/logout')
def logout():
    pass