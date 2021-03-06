#!/bin/bash

export PGPORT=8888
export PGHOST=/tmp

#Edit the path to your own PostGreSQL path if needed <path-to-sql>:${PATH}
export PATH="/usr/lib/postgresql/12/bin:${PATH}"

pip install flask flask-cors psycopg2
rm -rf $HOME/db412
initdb $HOME/db412
pg_ctl -D $HOME/db412 -o '-k /tmp' start
dropdb spotify_data
createdb spotify_data
psql -d spotify_data < tables.sql
python3 insertData.py
python3 app.py
pg_ctl -D $HOME/db412 -o '-k /tmp' stop
