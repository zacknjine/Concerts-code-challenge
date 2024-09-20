import sqlite3

# Database connection
def get_connection():
    connection = sqlite3.connect('concerts.db')
    connection.row_factory = sqlite3.Row  # This allows accessing columns by name
    return connection
