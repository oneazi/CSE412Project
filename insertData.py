import psycopg2
import csv

conn = psycopg2.connect(host='localhost', dbname='spotify_data', password='', user='', port=8888)

cur = conn.cursor()

artist_ids = []
# insert the Artist data into the Artist table
with open('csv/Artist.csv', 'r') as data_file:
    reader = csv.reader(data_file)
    next(reader) # Skip the header row.
    for row in reader:
        if row[0] not in artist_ids:
            artist_ids.append(row[0])
        else:
            continue
        cur.execute(
        "INSERT INTO Artist VALUES (%s, %s, %s, %s, %s)",
        row
    )

# insert the Label data into the Label table
with open('csv/Label.csv', 'r') as data_file:
    reader = csv.reader(data_file)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Label VALUES (%s, %s)",
        row
    )

album_ids = []
# insert the Album data into the album table
with open('csv/Album.csv', 'r') as data_file:
    reader = csv.reader(data_file)
    next(reader) # Skip the header row.
    for row in reader:
        if row[0] not in album_ids:
            album_ids.append(row[0])
        else:
            continue
        cur.execute(
        "INSERT INTO Album VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        row
    )    

track_ids = []
# insert the Track data into the Track table
with open('csv/Track.csv', 'r') as data_file:
    reader = csv.reader(data_file)
    next(reader) # Skip the header row.
    for row in reader:
        if row[0] not in track_ids:
            track_ids.append(row[0])
        else:
            continue
        cur.execute(
        "INSERT INTO Track VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        row
    )

conn.commit()

cur.close()
conn.close()