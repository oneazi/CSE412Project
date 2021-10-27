CREATE TABLE Label (
    LabelID INTEGER NOT NULL,
    LabelName TEXT,
    PRIMARY KEY(LabelID)
);

CREATE TABLE Artist (
    ArtistID TEXT NOT NULL,
    Popularity INTEGER,
    Followers INTEGER,
    Alias TEXT,
    Genre TEXT[],
    PRIMARY KEY(ArtistID)
);

CREATE TABLE Album (
    AlbumID TEXT NOT NULL,
    ArtistID TEXT NOT NULL,
    LabelID INTEGER,
    AlbumName TEXT,
    ReleaseDate TEXT,
    TotalTracks INTEGER,
    Popularity REAL,
    AlbumType TEXT,
    PRIMARY KEY(AlbumID),
    FOREIGN KEY(ArtistID) REFERENCES Artist ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(LabelID) REFERENCES Label ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Track (
    SongID TEXT NOT NULL,
    AlbumID TEXT NOT NULL,
    SongName TEXT,
    Instrumentalness REAL,
    Danceability REAL,
    Acousticness REAL,
    Speechiness REAL,
    Duration INTEGER,
    Loudness REAL,
    Tempo REAL,
    Valence REAL,
    PRIMARY KEY(SongID),
    FOREIGN KEY(AlbumID) REFERENCES Album ON DELETE CASCADE ON UPDATE CASCADE
);
