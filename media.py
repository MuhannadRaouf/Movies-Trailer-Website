import webbrowser


class Movie:
    # This is a class movie that describes the movies attributes.

    # Initializing the attributes of the class
    def __init__(self, movie_title, movie_storyline, poster_image,
                 movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    # Defining a method to show the trailer of the movie by using 'webbrowser' library's function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
