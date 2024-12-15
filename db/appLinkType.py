from db.connection import get_connection


# Create a new app link type
def create_app_link_type(description, app_url):
    """Insert a new app link type into the app_link_type table."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO app_link_type (description, app_url)
        VALUES (?, ?)
    ''', (description, app_url))

    connection.commit()
    connection.close()


# Retrieve all app link types
def get_all_app_link_types():
    """Fetch all app link types from the table."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM app_link_type')
    app_link_types = cursor.fetchall()

    connection.close()
    return [dict(row) for row in app_link_types]


# Retrieve a specific app link type by ID
def get_app_link_type_by_id(link_type_id):
    """Fetch an app link type by its ID."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM app_link_type WHERE id = ?', (link_type_id,))
    app_link_type = cursor.fetchone()

    connection.close()
    return dict(app_link_type) if app_link_type else None


# Update an app link type
def update_app_link_type(link_type_id, description, app_url):
    """Update the description and app_url of an app link type."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE app_link_type
        SET description = ?, app_url = ?
        WHERE id = ?
    ''', (description, app_url, link_type_id))

    connection.commit()
    connection.close()


# Delete an app link type
def delete_app_link_type(link_type_id):
    """Delete an app link type by its ID."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM app_link_type WHERE id = ?', (link_type_id,))

    connection.commit()
    connection.close()
