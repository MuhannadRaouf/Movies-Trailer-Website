import fresh_tomatoes   # importing a class that creates the front end of the project
import media    # importing a class that have the movie attributes

# The parameters of the instance is (MovieName, StoryLine, PosterImageUrl, TrailerUrl)
toy_story = media.Movie("Toy Story", "A boy that his toys comes a life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# The parameters of the instance is (MovieName, StoryLine, PosterImageUrl, TrailerUrl)
avatar = media.Movie("Avatar", "Soldiers volunteers to be a one of aliens brotherhood",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# The parameters of the instance is (MovieName, StoryLine, PosterImageUrl, TrailerUrl)
harry_potter = media.Movie("Harry Potter and the Philosopher's Stone",
                           "Young wizard who discovers his magical heritage as he makes close friends and a few "
                           "enemies in his first year at the Hogwarts School of Witchcraft and Wizardry.",
                           "https://vignette.wikia.nocookie.net/harrypotter/images/0/0e/Philostone.jpg/revision/latest/scale-to-width-down/338?cb=20170824190451",
                           "https://www.youtube.com/watch?v=eKSB0gXl9dw")

# The parameters of the instance is (MovieName, StoryLine, PosterImageUrl, TrailerUrl)
the_pianist = media.Movie("The Pianist", "Polish Jewish radio station pianist, sees Warsaw change gradually as World War II begins.",
                          "http://www.gstatic.com/tv/thumb/movieposters/30193/p30193_p_v8_ah.jpg",
                          "https://www.youtube.com/watch?v=u_jE7-6Uv7E")

# The parameters of the instance is (MovieName, StoryLine, PosterImageUrl, TrailerUrl)
assassin_creed = media.Movie("Assassin's Creed", "Cal Lynch travels back in time to 15th-century Spain through a revolutionary technology that unlocks the genetic memories contained in his DNA.",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcQpotWXc9_CqoWl19e0gXN8DUk5JxZbvTbxS6niDknxRFV7XHlz",
                             "https://www.youtube.com/watch?v=4haJD6W136c")

# The parameters of the instance is (MovieName, StoryLine, PosterImageUrl, TrailerUrl)
the_hateful_eight = media.Movie("The Hateful Eight", "While racing toward the town of Red Rock in post-Civil War "
                                                     "Wyoming, bounty hunter John Ruth and his fugitive prisoner "
                                                     "encounter another bounty hunter and a man who claims to be a "
                                                     "sheriff.",
                                "http://t2.gstatic.com/images?q=tbn:ANd9GcRQ4BYl9siQGuFuJoRU0k25bttWpjJfy7h46-xe-tRU4MMeROLQ",
                                "https://www.youtube.com/watch?v=gnRbXn4-Yis")

# List of the movies
movies = [toy_story, avatar, harry_potter, assassin_creed, the_hateful_eight, the_pianist]

# Using open method to get the movies and display it in a web site
fresh_tomatoes.open_movies_page(movies)
