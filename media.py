import webbrowser
from video import Video

#Movie class is a Video subclass
class Movie(Video):
    '''This class provide a way to store movie related information'''

    def __init__(self, movie_title, poster_image, youtube_trailer):
        Video.__init__(self, movie_title, youtube_trailer)
        self.poster_image_url = poster_image

    def show_trailer(self):
        '''Open up the browser and show the movie trailer on Youtube'''
        webbrowser.open(self.trailer_youtube_url)
        
    

