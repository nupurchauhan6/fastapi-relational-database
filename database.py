def create_user(cursor, user):
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))


def get_user(cursor, user_id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return cursor.fetchone()


def get_users(cursor):
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


def update_user(cursor, user_id, user):
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (user.name, user.email, user_id))


def delete_user(cursor, user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
