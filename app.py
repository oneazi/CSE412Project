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

# used for gettings artists according to most popular
@app.route("/artist/popularity")
def get_artist_by_pop():
    query = "SELECT Alias, Popularity FROM Artist ORDER BY Popularity DESC LIMIT 10;"
    cur.execute(sql.SQL(query))
    results = cur.fetchall()
    return jsonify({'results': results})

# used for gettings artists according to most followers
@app.route("/artist/followers")
def get_artist_by_followers():
    query = "SELECT Alias, Followers FROM Artist ORDER BY Followers DESC LIMIT 10;"
    cur.execute(sql.SQL(query))
    results = cur.fetchall()
    return jsonify({'results': results})

# used for getting albums according to most popular
@app.route("/album")
def get_album_by_pop():
    query = "SELECT A.AlbumName, A.Popularity, Artist.Alias \
        FROM Artist, (SELECT * FROM Album ORDER BY Popularity DESC LIMIT 10) as A \
        WHERE Artist.ArtistID=A.ArtistID ORDER BY Popularity DESC LIMIT 10;"
    cur.execute(sql.SQL(query))
    results = cur.fetchall()
    return jsonify({'results': results})

# used for getting albums according to most popular by a specific artist
@app.route("/album/artist")
def get_album_by_artist():
    artist = request.args.get('artist')
    query = "SELECT Album.AlbumName, Album.Popularity, Artist.Alias \
        FROM Artist, Album \
        WHERE Album.ArtistID = Artist.ArtistID AND Artist.Alias=%s ORDER BY Popularity DESC LIMIT 10;"
    cur.execute(sql.SQL(query), (artist,))
    results = cur.fetchall()
    return jsonify({'results': results})

app.run(debug=True, port=5000)