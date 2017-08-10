import webbrowser


class Movie:
    """
    Movie Trailers Website
    params:
    title(str): Title of movie_title
    img (str): Image from IMDB
    trailer(str): Movie trailer from youtube
    """

    def __init__(self, title, img, trailer):
        self.title = title  # set movie title
        self.img = img  # set poster image url
        self.trailer = trailer  # set trailer url
