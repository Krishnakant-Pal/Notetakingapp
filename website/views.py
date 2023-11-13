from flask import Blueprint, render_template,flash,redirect,request,url_for
from flask_login import login_required,current_user


from website.config import db

views = Blueprint('views', __name__)

@views.route('/',methods = ["GET", "POST"])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)< 1:
            flash('Note is too short',category='error')

        else:
            db.notes.insert_one({'note': note, 'user': current_user.email['email']})
            flash('Note added', category='success')
            return redirect(url_for('views.home'))
        print(current_user)
    cursor = db.notes.find({'user':current_user.email['email']})
    all_notes = []
    for note in cursor:
        all_notes.append(note['note'])
    return render_template('home.html',notes = all_notes, user = current_user)

