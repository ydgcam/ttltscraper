import sqlite3

def create_database():
    print("Starting database initialization...")

    connection = sqlite3.connect('./db/app.db')  # Connects or creates the database
    connection.execute("PRAGMA foreign_keys = ON;")  # Enable foreign key support
    cursor = connection.cursor()

    # Create a table for users
    print("Creating users table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            bio TEXT DEFAULT NULL,
            photo_url TEXT DEFAULT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create a table for app link types (must come before follower_links)
    print("Creating app_link_type table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS app_link_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            app_url TEXT NOT NULL
        )
    ''')

    # Create a table for users' following list
    print("Creating users_following_list table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users_following_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            followed_by_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            followed_date TIMESTAMP DEFAULT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (followed_by_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')

    # Create a table for follower links
    print("Creating follower_links table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS follower_links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            follower_id INTEGER NOT NULL,
            app_link_type_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (app_link_type_id) REFERENCES app_link_type(id) ON DELETE CASCADE
        )
    ''')

    connection.commit()
    connection.close()

    print("Finished database initialization")

if __name__ == '__main__':
    create_database()
