from db.connection import get_connection


# Create a new follower link
def create_follower_link(follower_id, app_link_type_id):
    """Insert a new follower link into the follower_links table."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO follower_links (follower_id, app_link_type_id)
        VALUES (?, ?)
    ''', (follower_id, app_link_type_id))

    connection.commit()
    connection.close()


# Retrieve all follower links
def get_all_follower_links():
    """Fetch all follower links from the table."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM follower_links')
    links = cursor.fetchall()

    connection.close()
    return [dict(link) for link in links]


# Retrieve follower links by follower_id
def get_follower_links_by_follower_id(follower_id):
    """Fetch all follower links for a specific follower."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM follower_links WHERE follower_id = ?', (follower_id,))
    links = cursor.fetchall()

    connection.close()
    return [dict(link) for link in links]


# Update a follower link
def update_follower_link(link_id, app_link_type_id):
    """Update the app_link_type_id for a specific follower link."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE follower_links
        SET app_link_type_id = ?
        WHERE id = ?
    ''', (app_link_type_id, link_id))

    connection.commit()
    connection.close()


# Delete a follower link
def delete_follower_link(link_id):
    """Delete a specific follower link by its ID."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM follower_links WHERE id = ?', (link_id,))

    connection.commit()
    connection.close()
