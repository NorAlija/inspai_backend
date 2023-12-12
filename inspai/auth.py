from .db import get_db
from mysql.connector.errors import IntegrityError
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
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
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        cursor = db.cursor()

        # Execute the query
        cursor.execute('SELECT user_id, password_hash FROM inspai_users WHERE email = %s', (email,))

        # Fetch the result
        user = cursor.fetchone()

        print(user)

        if user is None:
            error = 'Incorrect email or password.'
        elif not check_password_hash(user[1], password):  # Assuming password_hash is at index 1
            error = 'Incorrect email or password.'

        if error is None:
            session.clear()
            session['user_id'] = user[0]  # Assuming user_id is at index 0
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/login.html')




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
    return redirect(url_for('auth.login'))
