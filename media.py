import webbrowser

class Movie():
    ''' Movie Class to store movie info'''

    def __init__(self, movie_title, poster_image, trailer_youtube):
        ''' Constructor, initiate movie title, image and trailer'''
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
