import webbrowser


'''
import the webbroweser so you can open webpages in code.
Movie class
makes an object with title,storyline,image and youtube trailer
'''
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
        '''a movie should have these series of attribute'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        '''call on webbrowser class to open a the specific youtube url.'''
        webbrowser.open(self.trailer_youtube_url)
