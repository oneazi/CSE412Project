import requests
import json
import argparse
import csv
from CSVWriter import CSVWriter
from Deserializer import AudioFeatures
from Deserializer import ArtistAlbums
from Deserializer import Artist
from Deserializer import Track
from Deserializer import Album

#curl.exe -X "POST" -H "Authorization: Basic N2M1NzJmMDgzMDRiNDc0NmFkNDNiOWQ0NTc3YjhlOTk6ODRhNGJlNzgyMWFkNGVmNWJmYTg1ZmI0Njk4NTczZTE=" -d grant_type=client_credentials https://accounts.spotify.com/api/token

# ^^^ This is the command to get a 60 minute token to interact with the API. You will have to update line 13 in this file with the new token

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id",
                    default = '',
                    required = True)

# API information
token = "Bearer BQDW8w2LVJIjtwsgEi-g1XxesXFBRPsjkVeEiCei0Doefk46WnutS0Eh5HmXHd1qBBMzghG8JZrTcHhIVNc"
HEADERS = {"Authorization":token}

def main():
    args = parser.parse_args()
    artistID = args.id

    writer = CSVWriter()

    # Inserts artist entity into Artist.csv
    data = makeAPICall("https://api.spotify.com/v1/artists/" + artistID)
    artistRow = Artist.convertFromJson(json.dumps(data, indent=4))

    # Gets all the albums for the artist in a list
    data = makeAPICall("https://api.spotify.com/v1/artists/" + artistID + "/albums")
    artistIDAlbums = ArtistAlbums.convertFromJson(json.dumps(data, indent=4))

    if artistRow == -1 or artistIDAlbums == -1:
        print("Something went wrong - terminating. Try again maybe")
        print("If this error occured then no data was written to CSV files so it is safe to continue doing whatever.")
        sys.exit()

    writer.writeToCSV(artistRow, "Artist")

    # inserts album and track identities
    for albumID in artistIDAlbums:
        albumData = makeAPICall("https://api.spotify.com/v1/albums/" + albumID)
        albumRow = Album.convertFromJson(json.dumps(albumData, indent=4))
        labelName = Album.getRecordLabel(json.dumps(albumData, indent=4))
        if labelName == -1:
            print("error - label skipped")
        else:
            writer.addLabel(labelName)

        if albumRow == -1:
            print("error - album skipped")
        else:
            writer.writeToCSV(albumRow, "Album")

        

        trackIDs = Album.getTrackList(json.dumps(albumData, indent=4))
        for trackID in trackIDs:
            trackData = makeAPICall("https://api.spotify.com/v1/tracks/" + trackID)
            trackRow = Track.convertFromJson(json.dumps(trackData, indent=4))

            audioFeatureData = makeAPICall("https://api.spotify.com/v1/audio-features/" + trackID)
            audioFeaturesRow = AudioFeatures.convertFromJson(json.dumps(audioFeatureData, indent=4))
            if trackRow == -1 or audioFeaturesRow == -1:
                print("error - track skipped")
            else:
                for i in audioFeaturesRow:
                    trackRow.append(i)

                writer.writeToCSV(trackRow, "Track")

def makeAPICall(URL):
    r = requests.get(url = URL, headers = HEADERS)
    return r.json()


if __name__ == "__main__":
    main()
