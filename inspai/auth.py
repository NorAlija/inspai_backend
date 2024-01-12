from .db import get_db
from flask import jsonify
from mysql.connector.errors import IntegrityError
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__)

@bp.route('/signup', methods=['POST'])
def register():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    

    db = get_db()
    error = None

    if not first_name or not last_name:
        error = 'Name is required.'
    elif not email:
        error = "Email is required."
    elif not password:
        error = 'Password is required.'

    if error is None:
 
        cursor = db.cursor()
               # Check if the email already exists
        cursor.execute('SELECT user_id FROM inspai_users WHERE email = %s', (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            error = f"Email {email} is already registered."
        else:
            # If email doesn't exist, proceed with registration
            cursor.execute(
                "INSERT INTO inspai_users (first_name, last_name, email, password_hash) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, generate_password_hash(password)),
                )
            db.commit()
            return jsonify({'success': True})

        

    return jsonify({'error': error})


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    db = get_db()
    error = None
    cursor = db.cursor()

    # Execute the query
    cursor.execute('SELECT user_id, password_hash FROM inspai_users WHERE email = %s', (email,))

    # Fetch the result
    user = cursor.fetchone()

    if user is None:
        error = 'Incorrect email or password.'
    elif not check_password_hash(user[1], password):  # Assuming password_hash is at index 1
        error = 'Incorrect email or password.'

    if error is None:
        session.clear()
        session['user_id'] = user[0]  # Assuming user_id is at index 0
        return jsonify({'success': True, 'user_id': user[0]})

    return jsonify({'error': error})




@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db = get_db()
        cursor = db.cursor(dictionary=True)  # Use dictionary cursor for easier access to column values
        cursor.execute('SELECT * FROM inspai_users WHERE user_id = %s', (user_id,))
        g.user = cursor.fetchone()
        cursor.close()

@bp.route('/logout')
def logout():
    session.clear()
    return jsonify({'success': True})
