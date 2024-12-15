from connection import get_connection

def create_user(username, bio=None, photo_url=None):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO users (username, bio, photo_url) 
        VALUES (?, ?, ?)
    ''', (username, bio, photo_url))
    
    connection.commit()
    connection.close()

def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    
    connection.close()
    return [dict(user) for user in users]

def get_user_by_id(id: int):
    connection = get_connection()

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE users.id = ?', id)
    user = cursor.fetchall()

    connection.close()

    return dict(user) 

def get_user_by_username(name: str):
    connection = get_connection()

    cursor = connection.cursor()
    
    # Include wildcards in the parameter value
    cursor.execute('SELECT * FROM users WHERE users.username LIKE ?', (f"%{name}%",))
    
    user = cursor.fetchone()  # Assuming you expect a single user

    connection.close()

    # Return None if no user is found
    return dict(user) if user else None

def delete_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    
    connection.commit()
    connection.close()
