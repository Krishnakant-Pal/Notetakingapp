from flask import Blueprint, render_template
from flask_login import login_required,current_user




views = Blueprint('views', __name__)

@views.route('/',methods = ["GET", "POST"])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)< 1:
            flash('Note is too short',category='error')

        else:
            db.notes.insert_one({'note': note, 'user': current_user.email})
            flash('Note added', category='success')
            return redirect(url_for('views.home'))
        
    return render_template('home.html',user = current_user)

