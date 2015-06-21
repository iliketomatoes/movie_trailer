'''Here we create the list of movies and we store them into a list'''

import fresh_tomatoes
import media

forrest_gump = media.Movie("Forrest Gump",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=Bp_azVkZxHk"
)


life_is_beautiful = media.Movie("Life is beautiful",
    "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
    "https://www.youtube.com/watch?v=64ZoO7oiN0s"
)

back_to_the_future = media.Movie("Back to the future",
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg",
    "https://www.youtube.com/watch?v=AVBMsylM_xA"
)

ghostbusters = media.Movie("Ghostbusters",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Ghostbusters_cover.png/220px-Ghostbusters_cover.png",
    "https://www.youtube.com/watch?v=vntAEVjPBzQ"
)

inglorious_basterds = media.Movie("Inglourious Basterds",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Inglourious_Basterds_poster.jpg/220px-Inglourious_Basterds_poster.jpg",
    "https://www.youtube.com/watch?v=BQ0HADX2a24"
)

mediterraneo = media.Movie("Mediterraneo",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Mediterraneo_sheet.jpg",
    "https://www.youtube.com/watch?v=d04cySd7ZOQ"
)


movies = [forrest_gump, life_is_beautiful, back_to_the_future, ghostbusters, inglorious_basterds, mediterraneo]

fresh_tomatoes.open_movies_page(movies)
