# CONCERT CODE CHALLENGE

## Description
This project manages a concert domain with three main entities: Bands, Venues, and Concerts. It implements a many-to-many relationship between Bands and Venues using raw SQL queries.

### Getting Started
To get a local copy up and running, follow these simple steps:

# Prerequisites
* Python3
* SQLite3 library

## Installation
1. Clone the repository using the SSH key provided below:
   ```bash
   git@github.com:zacknjine/concert-code-challenge.git

2. If you don't have SQLite3 installed, you can do so by opening you terminal and runnning:
* sudo apt install sqlite3

#### Usage

1. Create the database and tables using raw SQL commands.

2. Define the schema for the concerts table, establishing relationships with Bands and Venues.

3. Implement the following methods:

  ** Concert Methods

     Concert.band()
     Concert.venue()
     Concert.hometown_show()
     Concert.introduction()


  ** Venue Methods

      Venue.concerts()
      Venue.bands()
      Venue.concert_on(date)
      Venue.most_frequent_band()


 *** Band Methods

      Band.concerts()
      Band.venues()
      Band.play_in_venue(venue, date)
      Band.all_introductions()
      Band.most_performances()



##### License

This project is licensed under the MIT License, see the LICENSE file for details.
