import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager


def add_user(name, password):
    connection = sqlite3.connect('app/app.db', check_same_thread=False)
    cursor = connection.cursor()
    msg = ''
    try:
        cursor.execute(f"""INSERT INTO users
                        (name, password) VALUES
                        {(name, generate_password_hash(password))}""")
        connection.commit()
        msg = "SUCCESS"
    except Exception as er:
        connection.rollback()
        msg = f'{er}'
    finally:
        connection.close()
        return msg


def get_all_users():
    connection = sqlite3.connect('app/app.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * from users')
    all_tests = cursor.fetchall()
    print(all_tests)
    return all_tests


def user_signing_checking(name, password):
    for i in get_all_users():
        user_name = i[1]
        if name == user_name:
            if check_password_hash(i[2], password):
                return True
    return False


@login_manager.user_loader
def load_user(user_id):
    for i in get_all_users():
        if user_id == i[0]:
            return i

