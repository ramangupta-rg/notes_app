from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user
from .models import User, Note
from .forms import LoginForm, NoteForm
from . import app, db

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic here
    pass

@app.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    # Add, edit, delete notes logic
    pass

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
