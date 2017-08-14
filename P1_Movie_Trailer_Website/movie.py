import media
import fresh_tomatoes

t1 = "https://www.youtube.com/watch?v=2TAOizOnNPo"
t2 = "https://www.youtube.com/watch?v=F_VIM03DXWI"
t3 = "https://www.youtube.com/watch?v=mw2AqdB5EVA"
# Create movie objects
movie_1 = media.Movie(title="The Fast and the Furious",
                      poster_image_url="http://bit.ly/2vToD9o",
                      trailer_youtube_url=t1)

movie_2 = media.Movie(title="2 Fast 2 Furious",
                      poster_image_url="http://bit.ly/2vqR3VR",
                      trailer_youtube_url=t2)

movie_3 = media.Movie(title="Fast Five",
                      poster_image_url="http://bit.ly/2wyuzT4",
                      trailer_youtube_url=t3)


if __name__ == "__main__":
    movies = [movie_1, movie_2, movie_3]  # create movies array
    fresh_tomatoes.open_movies_page(movies)  # open all movies
