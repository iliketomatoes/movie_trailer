import urllib
import json

class Video():

    def __init__(self, title, youtube_trailer):
        self.title = title
        self.trailer_youtube_url = youtube_trailer
        self.findRemoteData()

    def findRemoteData(self):
        params = urllib.urlencode({'t': self.title, 'plot': 'short', 'r': 'json'})
        response = urllib.urlopen("http://www.omdbapi.com/?%s" % params)
        output = json.load(response)
        self.year = output['Year']
        self.rating = output['imdbRating']
        self.plot = output['Plot']
        print output
    
