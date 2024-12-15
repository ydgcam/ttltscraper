import sqlite3

DATABASE = "./db/app.db"

def get_connection():
    """Get a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE)

    # Enables dict-like access
    connection.row_factory = sqlite3.Row
      
    return connection
