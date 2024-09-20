# Description
A simple README explaining how you should set up the database and run the project.

## Getting Started

Before running your app, you should apply your migrations by executing the SQL files in your SQLite database with the code below;

    * sqlite3 concerts.db < migrations/create_bands_table.sql
    * sqlite3 concerts.db < migrations/create_venues_table.sql
    * sqlite3 concerts.db < migrations/create_concerts_table.sql

The code above will set up your database schema and allow you to run the Python queries later.

### HAPPY CODING!!