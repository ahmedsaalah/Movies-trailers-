import webbrowser
class Movie():
    '''
    This class consists of main attributes of the movies
    '''
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """
               constructor

                Args:
                    movie_title (str): this will carry the title of the movie .
                    movie_storyline (str): Description of the movie .
                    poster_image (str): Url of the poster .
                    trailer_youtube(str): trailer url on youtube

        """
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube






