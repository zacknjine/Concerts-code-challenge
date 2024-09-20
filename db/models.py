class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date
