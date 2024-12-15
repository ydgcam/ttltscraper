from connection import get_connection

def add_following(followed_by_id, username, followed_date=None):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO users_following_list (followed_by_id, username, followed_date) 
        VALUES (?, ?, ?)
    ''', (followed_by_id, username, followed_date))
    
    connection.commit()
    connection.close()

def get_following_list(followed_by_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM users_following_list WHERE followed_by_id = ?', (followed_by_id,))
    following = cursor.fetchall()
    
    connection.close()
    return [dict(entry) for entry in following]

def add_following_batch(following_data):
    """
    Perform a batch insert into the users_following_list table.

    :param following_data: List of tuples (followed_by_id, username, followed_date)
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.executemany('''
        INSERT INTO users_following_list (followed_by_id, username, followed_date)
        VALUES (?, ?, ?)
    ''', following_data)

    connection.commit()
    connection.close()
