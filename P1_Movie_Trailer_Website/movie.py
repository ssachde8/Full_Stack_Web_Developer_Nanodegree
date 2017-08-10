import media
import fresh_tomatoes

# Create movie objects
m1 = media.Movie(title="The Fast and the Furious", img="http://bit.ly/2vToD9o",
                 trailer="https://www.youtube.com/watch?v=2TAOizOnNPo")

m2 = media.Movie(title="2 Fast 2 Furious", img="http://bit.ly/2vqR3VR",
                 trailer="https://www.youtube.com/watch?v=F_VIM03DXWI")

m3 = media.Movie(title="Fast Five", img="http://bit.ly/2wyuzT4",
                 trailer="https://www.youtube.com/watch?v=mw2AqdB5EVA")

if __name__ == "__main__":
    movies = [m1, m2, m3]  # create movies array
    fresh_tomatoes.open_movies_page(movies)  # open all movies
