/*Selection Queries*/
SELECT * FROM Track WHERE ORDER BY Track.Acousticness DESC LIMIT 10;

/*Query for the most danceable songs by a specific artist*/
SELECT T.Alias, T.AlbumName, Label.LabelName, T.SongName, T.Danceability
FROM Label, (SELECT * FROM Track, Album, Artist 
                WHERE Track.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Artist.Alias=''
                ORDER BY Track.Danceability DESC LIMIT 10) as T
WHERE T.LabelID = Label.LabelID
ORDER BY T.Danceability DESC;

/*Get the artist name, label name, song name, album name, and acousticness of the top 10 most acoustic songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Acousticness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Acousticness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Acousticness DESC;

/*Get the artist name, label name, song name, album name, and instrumentalness of the top 10 most instrumental songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Instrumentalness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Instrumentalness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Instrumentalness DESC;

/*Get the artist name, label name, song name, album name, and danceability of the top 10 most danceable songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Danceability
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Danceability DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Danceability DESC;

/*Get the artist name, label name, song name, album name, and speechiness of the top 10 most speechy songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Speechiness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Speechiness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Speechiness DESC;

/*Get the artist name, label name, song name, album name, and duration of the top 10 longest songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Duration
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Duration DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Duration DESC;

/*Get the artist name, label name, song name, album name, and loudness of the top 10 loudest songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Loudness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Loudness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Loudness DESC;

/*Get the artist name, label name, song name, album name, and tempo of the top 10 fastest songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Tempo
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Tempo DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Tempo DESC;

/*Get the artist name, label name, song name, album name, and valence of the top 10 happiest songs*/
SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Valence
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Valence DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Valence DESC;

/*Get artist information for the top 10 most popular artists*/
SELECT * FROM Artist ORDER BY Popularity DESC LIMIT 10;

/*Get artist information for the top 10 artists with the most followers*/
SELECT * FROM Artist ORDER BY Followers DESC LIMIT 10;

/*Get artist name and album information for the top 10 most popular albums*/
SELECT A.*, Artist.Alias
FROM Artist, (SELECT * FROM Album ORDER BY Popularity DESC LIMIT 10) as A
WHERE Artist.ArtistID=A.ArtistID ORDER BY Popularity DESC;

/*Deletion Queries*/
DELETE FROM Artist WHERE Alias='Maroon 5';

DELETE FROM Label WHERE LabelID=1;

DELETE FROM Album WHERE AlbumName='Spotify Singles: Paul McCartney Box Set';

DELETE FROM TRACK WHERE SongName='Overdrive';

/*Update Queries*/
UPDATE Artist SET Followers=Followers+100 WHERE Artist.ArtistID='4STHEaNw4mPZ2tzheohgXB';

/*Insertion*/
INSERT INTO Artist VALUES ('100', 1, 1, 'test', '{rock}');

INSERT INTO Label VALUES (1000, 'Some Label');

INSERT INTO Album VALUES ('abcdefg', '100', 1000, 'Album Name', '01/01/2000', 10, 96, 'album');

INSERT INTO Track VALUES ('trackid', 'abcdefg', 'Some Song', 0.5, 0.5, 0.5, 0.5, 100, 0.5, 0.5, 0.5);