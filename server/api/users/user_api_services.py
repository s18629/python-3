import bcrypt
from sqlite3 import Cursor
import re

LOGIN_RE = r'^[a-zA-Z0-9]+$'


def validate_password(password):
    return len(password) > 4


def has_user(db: Cursor, login: str):
    return len(db.execute("SELECT * FROM users WHERE login = ?", (login,)).fetchall()) > 0


def create_user(db: Cursor, login: str, password):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    db.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login.lower(), password))


def validate_login(login: str):
    if not len(login) > 3:
        return False

    return re.match(LOGIN_RE, login) is not None
