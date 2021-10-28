/*Selection Queries*/
SELECT * FROM Track WHERE ORDER BY Track.Acousticness DESC LIMIT 10;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Acousticness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Acousticness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Acousticness DESC;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Instrumentalness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Instrumentalness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Instrumentalness DESC;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Danceability
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Danceability DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Danceability DESC;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Speechiness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Speechiness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Speechiness DESC;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Duration
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Duration DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Duration DESC;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Loudness
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Loudness DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Loudness DESC;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Tempo
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Tempo DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Tempo DESC;

SELECT Artist.Alias, Album.AlbumName, Label.LabelName, T.SongName, T.Valence
FROM Artist, Album, Label, (SELECT * FROM Track ORDER BY Track.Valence DESC LIMIT 10) as T
WHERE T.AlbumID=Album.AlbumID AND Album.ArtistID=Artist.ArtistID AND Album.LabelID = Label.LabelID
ORDER BY T.Valence DESC;

SELECT * FROM Artist ORDER BY Popularity DESC LIMIT 10;

SELECT * FROM Artist ORDER BY Followers DESC LIMIT 10;

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