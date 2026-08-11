from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import login_required, current_user
from . import db
import json

from website.models import Note


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("girl write something", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("note added", category='success')
    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/edit-note', methods=['POST'])
@login_required
def edit_note():
    payload = json.loads(request.data)
    noteId = payload.get('noteId')
    new_data = payload.get('data') or payload.get('note')
    note = Note.query.get(noteId)
    if note and new_data is not None:
        if note.user_id == current_user.id:
            if len(new_data) < 1:
                flash("girl write something", category='error')
            else:
                note.data = new_data
                db.session.commit()
                flash("note updated", category='success')
    return jsonify({})