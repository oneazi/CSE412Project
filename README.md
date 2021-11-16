# SpotifyCSE412
Group project for CSE 412

## Prerequisites
* Python 3.9
* Psycopg2
* PostgreSQL
* System Requirements: WSL2, MacOS, Linux
* Flask `pip install flask`

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
