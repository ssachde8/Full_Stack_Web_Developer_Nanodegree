import media
import fresh_tomatoes

movie_1 = media.Movie(title="The Fast and the Furious", poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BNzlkNzVjMDMtOTdhZC00MGE1LTkxODctMzFmMjkwZmMxZjFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg", 
trailer_youtube_url="https://www.youtube.com/watch?v=2TAOizOnNPo")

movie_2 = media.Movie(title="2 Fast 2 Furious", poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMzExYjcyYWMtY2JkOC00NDUwLTg2OTgtMDI3MGY2OWQzMDE2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg", 
trailer_youtube_url="https://www.youtube.com/watch?v=F_VIM03DXWI")

movie_3 = media.Movie(title="Fast Five", poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNTk5MTE0OF5BMl5BanBnXkFtZTcwMjA2NzY3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg", trailer_youtube_url="https://www.youtube.com/watch?v=mw2AqdB5EVA")


if __name__ == "__main__":
	movies = [movie_1, movie_2, movie_3]
	fresh_tomatoes.open_movies_page(movies)