from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, send
from database import init_db, register_user, get_user
import bcrypt
import sqlite3

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
socketio = SocketIO(app)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('chat'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['username'] = username
            return redirect(url_for('chat'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            register_user(username, hashed_password)
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return 'Username already exists'
    return render_template('register.html')

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', username=session['username'])

@socketio.on('message')
def handle_message(msg):
    username = session.get('username')
    send(f'{username}: {msg}', broadcast=True)

if __name__ == '__main__':
    init_db()
    socketio.run(app, debug=True)
