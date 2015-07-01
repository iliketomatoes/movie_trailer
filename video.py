import urllib
import json

class Video():
    '''This class provide a way to retrieve movie related data from omdapi'''

    def __init__(self, title, youtube_trailer):
        self.title = title
        self.trailer_youtube_url = youtube_trailer
        #Let's get some additional info, i.e. year, rating and plot
        additional_data = self.find_remote_data()
        self.year = additional_data['Year']
        self.rating = additional_data['imdbRating']
        self.plot = additional_data['Plot']
            
    def find_remote_data(self):
        '''Fetch year, rating and plot of each movie from http://www.omdbapi.com/'''
        params = urllib.urlencode({'t': self.title, 'plot': 'short', 'r': 'json'})
        response = urllib.urlopen("http://www.omdbapi.com/?%s" % params)
        output = json.load(response)
        return output
