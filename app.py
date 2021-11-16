# this file runs a flask server which will act as the backend to our application
# All queries to the database will be handled using API requests 

from flask import Flask, jsonify, request, render_template
import psycopg2
from psycopg2 import sql

# initialize flask server
app = Flask(__name__)

# initialize connection to db
conn = psycopg2.connect(host='localhost', dbname='spotify_data', password='', user='', port=8888)
cur = conn.cursor()

@app.route("/spotifyData")
def hello_world():
    parameter = request.args.get('parameter').lower()
    print(parameter)
    query = "SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.{}\
            FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.{} DESC LIMIT 10) as T\
            WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID\
            ORDER BY T.{} DESC;"
    cur.execute(sql.SQL(query).format(sql.Identifier(parameter), sql.Identifier(parameter), sql.Identifier(parameter)))
    results = cur.fetchall()
    return jsonify({'results': results})

app.run(debug=True)