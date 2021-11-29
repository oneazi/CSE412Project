# SpotifyCSE412
Group project for CSE 412

## Prerequisites
* Python 3.9
* Psycopg2
* PostgreSQL
* System Requirements: WSL2, MacOS, Linux
* Flask `pip install flask flask-cors`
* Visual Studio Code with Live Server Extension

## Steps to Run
1. Configure insertData.py to connect to you local instance of the database
    * Add your PostgreSQL username and password to the `user` and `password` parameters on line 5
2. After installing all the prerequisites, run the following commands in order
    * `initdb $HOME/db412` 
        > (`rm -rf $HOME/db412` if this directory already exists)
    * `pg_ctl -D $HOME/db412 -o '-k /tmp' start`
    * `dropdb spotify_data`
    * `createdb spotify_data`
    * `psql -d spotify_data < tables.sql`
    * `python3 insertData.py`
    * `python3 app.py`
3. Open the directory containing `index.html` in Visual Studio Code and run the webpage using Live Server

## Functionality
1. Search using the provided metrics and provide an artist name for more specif results. Click search to load the results.
2. Hover over bars to see more detailed information about the artists, songs, or albums
3. Clicking on a bar will open a new tab which will search for the selected song, album, or artist on google