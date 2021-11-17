# this file runs a flask server which will act as the backend to our application
# All queries to the database will be handled using API requests 
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import psycopg2
from psycopg2 import sql

# initialize flask server
app = Flask(__name__)
CORS(app)

# initialize connection to db
conn = psycopg2.connect(host='localhost', dbname='spotify_data', password='', user='', port=8888)
cur = conn.cursor()

# used for getting songs according to a metric without any artist specified
@app.route("/metric")
def get_tracks():
    metric = request.args.get('metric').lower()
    query = "SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.{}\
            FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.{} DESC LIMIT 10) as T\
            WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID\
            ORDER BY T.{} DESC;"
    cur.execute(sql.SQL(query).format(sql.Identifier(metric), sql.Identifier(metric), sql.Identifier(metric)))
    results = cur.fetchall()
    return jsonify({'results': results})

# used for getting songs according to a metric and artist
@app.route("/metric/artist")
def get_tracks_by_artist():
    metric = request.args.get('metric').lower()
    artist = request.args.get('artist')
    query = "SELECT T.Alias, T.AlbumName, Label.LabelName, T.SongName, T.{}\
            FROM Label, (SELECT * FROM Track, Album, Artist \
                            WHERE Track.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Artist.Alias=%s\
                            ORDER BY Track.{} DESC LIMIT 10) as T\
            WHERE T.LabelID = Label.LabelID\
            ORDER BY T.{} DESC;"
    cur.execute(sql.SQL(query).format(sql.Identifier(metric), sql.Identifier(metric), sql.Identifier(metric)), (artist,))
    results = cur.fetchall()
    return jsonify({'results': results})

# TODO: Add endpoints with queries for top artists ('/artist'), top albums ('/album'),
#  and albums for a specified artist ('/album/artist')

app.run(debug=True)