import webbrowser


class Movie:
    """
    Movie Trailers Website
    params:
    title(str): Title of movie_title
    poster_image_url (str): Image from IMDB
    trailer_youtube_url(str): Movie trailer from youtube
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title  # set movie title
        self.poster_image_url = poster_image_url  # set poster image url
        self.trailer_youtube_url = trailer_youtube_url  # set trailer url
