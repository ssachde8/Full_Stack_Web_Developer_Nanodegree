import webbrowser

class Movie():
	"""
	Movie Trailers Website
	params:
	title(str): Title of movie_title
	poster_image_url (str): Image from IMDB
	trailer_youtube_url(str): Movoe trailer from youtube
	"""
	
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url  = poster_image_url 
		self.trailer_youtube_url = trailer_youtube_url