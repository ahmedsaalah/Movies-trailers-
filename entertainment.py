import movie
import fresh_tomatoes

# make object and send data of movies

Requiem_for_a_Dream = movie.Movie("Requiem for a Dream",
                                  "Requiem for a Dream is a 2000 American"
                                  " psychological drama film directed by"
                                  " Darren Aronofsky and starring Ellen"
                                  " Jared Leto, Jennifer Connelly,"
                                  " and Marlon Wayans",
                                  "https://upload.wikimedia.org"
                                  "/wikipedia/en/9/92/"
                                  "Requiem_for_a_dream.jpg",
                                  "https://www.youtube.com/"
                                  "watch?v=jzk-lmU4KZ4")
Shutter_Island = movie.Movie("Shutter Island",
                             "a U.S. marshal investigates"
                             " the disappearance of a murderess who"
                             " escaped from a hospital for"
                             " the criminally insane",
                             "http://www.gstatic.com/tv/thumb/"
                             "movieposters/3531967/p3531967_p_v8_ah.jpg",
                             "https://www.youtube.com/watch?v=5iaYLCiq5RM")
Inglourious_Basterds = movie.Movie("Inglourious Basterds",
                                   "American-German war film written and"
                                   " directed by Quentin Tarantino"
                                   " starring Brad Pitt",
                                   "https://ingloriousbastards1.files."
                                   "wordpress.com/2012/12/"
                                   "inglourious-basterds9.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=KnrRy6kSFF0")

# create array movies contains all your favorite movies
movies = [Shutter_Island, Requiem_for_a_Dream, Inglourious_Basterds]
# function open_movies_page take the array of movies
fresh_tomatoes.open_movies_page(movies)
