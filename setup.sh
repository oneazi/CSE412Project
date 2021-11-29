#!/bin/bash

export PGPORT=8888
export PGHOST=/tmp
export PATH="/usr/lib/postgresql/12/bin:${PATH}"

rm -rf $HOME/db412
initdb $HOME/db412
pg_ctl -D $HOME/db412 -o '-k /tmp' start
dropdb spotify_data
createdb spotify_data
psql -d spotify_data < tables.sql
python3 insertData.py
python3 app.py
