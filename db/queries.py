from db.connection import get_connection

def get_concert_band(concert_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT bands.* FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.id = ?
    '''
    cursor.execute(query, (concert_id,))
    return cursor.fetchone()

def get_concert_venue(concert_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT venues.* FROM venues
    JOIN concerts ON venues.id = concerts.venue_id
    WHERE concerts.id = ?
    '''
    cursor.execute(query, (concert_id,))
    return cursor.fetchone()

def get_venue_concerts(venue_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT concerts.* FROM concerts
    WHERE concerts.venue_id = ?
    '''
    cursor.execute(query, (venue_id,))
    return cursor.fetchall()

def get_venue_bands(venue_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT DISTINCT bands.* FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.venue_id = ?
    '''
    cursor.execute(query, (venue_id,))
    return cursor.fetchall()

def get_band_concerts(band_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT concerts.* FROM concerts
    WHERE concerts.band_id = ?
    '''
    cursor.execute(query, (band_id,))
    return cursor.fetchall()

def get_band_venues(band_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT DISTINCT venues.* FROM venues
    JOIN concerts ON venues.id = concerts.venue_id
    WHERE concerts.band_id = ?
    '''
    cursor.execute(query, (band_id,))
    return cursor.fetchall()

def is_hometown_show(concert_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT bands.hometown, venues.city FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    '''
    cursor.execute(query, (concert_id,))
    result = cursor.fetchone()
    return result['hometown'] == result['city']

def concert_introduction(concert_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT bands.name, bands.hometown, venues.city FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    '''
    cursor.execute(query, (concert_id,))
    result = cursor.fetchone()
    return f"Hello {result['city']}!!!!! We are {result['name']} and we're from {result['hometown']}"

def band_play_in_venue(band_id, venue_id, date):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    INSERT INTO concerts (band_id, venue_id, date)
    VALUES (?, ?, ?)
    '''
    cursor.execute(query, (band_id, venue_id, date))
    connection.commit()

def band_most_performances():
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT bands.name, COUNT(concerts.id) AS concert_count FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    GROUP BY bands.name
    ORDER BY concert_count DESC
    LIMIT 1
    '''
    cursor.execute(query)
    return cursor.fetchone()

def venue_most_frequent_band(venue_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''
    SELECT bands.name, COUNT(concerts.id) AS performance_count FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    WHERE concerts.venue_id = ?
    GROUP BY bands.name
    ORDER BY performance_count DESC
    LIMIT 1
    '''
    cursor.execute(query, (venue_id,))
    return cursor.fetchone()
