import json

# Every JSON response has its own class in this file. This will eventually have every entity too
#
# Explanation: 
# Every class has two methods...
# The def __init__ constructor HAS TO have every property of the JSON response
# The convertFromJson method does the actual work. 
# 
# An example of interacting with this class would look like this:
#
# deserializedAlbumInformation = Album.convertFromJson(json.dumps(data, indent=4)) #where 'data' is the json response
# albumId = deserializedAlbumInformation.id
# albumPopularity = deserializedAlbumInformation.popularity
# ...
#

class Artist:
    def __init__(self, external_urls, followers, genres, href, id, images, name, popularity, type, uri):
        self.external_urls = external_urls
        self.followers = followers
        self.genres = genres
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.popularity = popularity
        self.type = type
        self.uri = uri

    @classmethod
    def convertFromJson(cls, JSONString):
        JSONDict = json.loads(JSONString)
        try:
            user = cls(**JSONDict)

            row = [str(user.id), str(user.name), str(user.popularity), str(user.followers['total']), str(user.genres)]
            return row
        except: 
            print("504 Error occured - Artist")
            return -1

class ArtistAlbums:
    def __init__(self, href, items, limit, next, offset, previous, total):
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.offset = offset
        self.previous = previous
        self.total = total

    @classmethod
    def convertFromJson(cls, JSONString):
        JSONDict = json.loads(JSONString)
        try:
            user = cls(**JSONDict)
            

            albumNameList = []
            for i in range(len(user.items)):
                albumNameList.append(user.items[i]['name'])

            albumIDList = []
            for i in range(len(user.items)):
                albumIDList.append(user.items[i]['id'])

            albumDict = {}
            index = 0
            for name in albumNameList:
                albumDict.update({albumNameList[index]: albumIDList[index]})
                index = index + 1

            officialIDList = []
            for val in albumDict:
                officialIDList.append(albumDict[val])

            return officialIDList
        except: 
            print("504 Error occured - Artist Albums")
            return -1

class Album:
    def __init__(self, album_type, artists, available_markets, copyrights, external_ids, external_urls, genres, href, id, images, name, popularity, release_date, release_date_precision, tracks, type, uri, label, total_tracks):
        self.album_type = album_type
        self.artists = artists
        self.available_markets =available_markets 
        self.copyrights = copyrights
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.genres = genres
        self.href = href
        self.id = id
        self.images = images 
        self.name = name
        self.popularity = popularity
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.tracks = tracks
        self.type = type
        self.uri = uri
        self.label = label
        self.total_tracks = total_tracks

    @classmethod
    def convertFromJson(cls, JSONString):
        JSONDict = json.loads(JSONString)
        try:
            user = cls(**JSONDict)

            # Extracts Artist name 
            for i in range(len(user.artists)):
                artistName = user.artists[i]['name']

            row = [str(user.id), str(user.name), str(user.release_date), str(user.total_tracks), str(user.popularity), str(user.type)]
            return row
        except: 
            print("504 Error occured - Album")
            return -1

    @classmethod
    def getTrackList(cls, JSONString):
        JSONDict = json.loads(JSONString)
        try:
            user = cls(**JSONDict)

            trackList = []
            for i in range(len(user.tracks['items'])):
                trackList.append(user.tracks['items'][i]['id'])

            return trackList
        except: 
            print("504 Error occured - Get Track List")
            return -1
    
    @classmethod
    def getRecordLabel(cls, JSONString):
        JSONDict = json.loads(JSONString)
        
        try:
            user = cls(**JSONDict)

            return user.label
        except: 
            print("504 Error occured - Get Record Label")
            return -1

class Track:
    def __init__(self, album, artists, available_markets, disc_number, duration_ms, explicit, external_ids, external_urls, href, id, is_local, name, popularity, preview_url, track_number, type, uri):
        self.album = album
        self.artists = artists
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.is_local = is_local
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri


    @classmethod
    def convertFromJson(cls, JSONString):
        JSONDict = json.loads(JSONString)
        try:
            user = cls(**JSONDict)

            row = [str(user.id), str(user.name)]

            return row
        except: 
            print("504 Error occured - Track")
            return -1



class AudioFeatures:
    def __init__(self, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, type, id, uri, track_href, analysis_url, duration_ms, time_signature):
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.type = type
        self.id = id
        self.uri = uri
        self.track_href = track_href
        self.analysis_url = analysis_url
        self.duration_ms = duration_ms
        self.time_signature = time_signature

    @classmethod
    def convertFromJson(cls, JSONString):
        JSONDict = json.loads(JSONString)
        try:
            user = cls(**JSONDict)

            row = [str(user.duration_ms), str(user.instrumentalness), str(user.danceability), str(user.acousticness), str(user.speechiness), str(user.loudness), str(user.tempo), str(user.valence)]

            return row
        except: 
            print("504 Error occured - Audio Features")
            return -1
