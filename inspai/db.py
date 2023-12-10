import mysql.connector
from flask import current_app, g
from click import command, echo

def get_db():
    if "db" not in g:
        # Connect to MySQL using the configured parameters
        g.db = mysql.connector.connect(
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            host=current_app.config['MYSQL_HOST'],
            database=current_app.config['MYSQL_DB']
        )
        g.db.row_factory = mysql.connector.cursor.MySQLCursorDict

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()



def init_app(app):
    app.teardown_appcontext(close_db)

