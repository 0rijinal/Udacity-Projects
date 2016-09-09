''' import fresh_tomatoes.py and media.py must be in same folder '''
import fresh_tomatoes
import media

''' the format is movie title, storyline, posterimg, youtube trailer '''
transformers = media.Movie("Transformers",
                           "Transformers is robots in disguise.",
                           "http://www.gstatic.com/tv/thumb/movieposters/159729/p159729_p_v8_al.jpg",
                           "https://www.youtube.com/watch?v=QZLgiwYP5to")

soul_surfer = media.Movie("soul surfer",
                            "Teenage surfer Bethany Hamilton overcomes the odds and her own fears of returning to the water after losing her left arm in a shark attack.",
                            "http://www.sonypictures.com/movies/soulsurfer/assets/images/onesheet.jpg",
                            "https://www.youtube.com/watch?v=MWeOjBCi3c4")

a21jumpstreet = media.Movie("21 jump street",
                            "A pair of underachieving cops are sent back to a local high school to blend in and bring down a synthetic drug ring.",
                            "https://atomicfangirl.files.wordpress.com/2012/03/21-jump-street.jpg",
                            "https://www.youtube.com/watch?v=RLoKtb4c4W0")

x_men_apocalypse = media.Movie("X men apocalypse",
                            "American superhero film based on the fictional X-Men characters that appear in Marvel Comics.",
                            "http://blogs-images.forbes.com/scottmendelson/files/2016/05/X-Men-Apocalypse-launch-quad-poster-1200x903.jpg",
                            "https://www.youtube.com/watch?v=COvnHv42T-A")

jurassic_world = media.Movie("Jurassic World", "Teenage surfer Bethany Hamilton overcomes the odds and her own fears of returning to the water after losing her left arm in a shark attack.",
                           "https://i.ytimg.com/vi/aJJrkyHas78/maxresdefault.jpg",
                           "https://www.youtube.com/watch?v=RFinNxS5KN4")

divergent = media.Movie("Divergent",
                        "In a world divided by factions based on virtues, Tris learns she's Divergent and won't fit in. ",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")

''' a container to hold the title of each movie. '''
movies =[transformers, soul_surfer, a21jumpstreet, x_men_apocalypse, jurassic_world, divergent]

''' open the list of movies to browser. '''
fresh_tomatoes.open_movies_page(movies)
