import sqlite3
from db.queries import *

# Function to apply migrations (create tables)
def run_migrations():
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Create the bands table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hometown TEXT NOT NULL
    );
    ''')

    # Create the venues table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        city TEXT NOT NULL
    );
    ''')

    # Create the concerts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_id INTEGER NOT NULL,
        venue_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (band_id) REFERENCES bands(id),
        FOREIGN KEY (venue_id) REFERENCES venues(id)
    );
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    # Run migrations
    run_migrations()

    # Example of getting a concert's band and venue
    concert_id = 1
    print(get_concert_band(concert_id))
    print(get_concert_venue(concert_id))

    # Example of playing in a venue
    band_id = 1
    venue_id = 2
    date = '2024-09-25'
    band_play_in_venue(band_id, venue_id, date)
