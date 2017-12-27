import fresh_tomatoes
import media
#Creating Different Movie Object and proving the values as per the constructor
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toy that comes to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
lagaan = media.Movie("Lagaan",
                     "The people of a small village in Victorian India stake their future on a game of cricket against their ruthless British rulers.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg",
                     "https://www.youtube.com/watch?v=oSIGQ0YkFxs")
kahaani = media.Movie("Kahaani 2",
                      "A woman with a mysterious past is charged with kidnapping and murder",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Kahaani_2_film_poster.jpg/220px-Kahaani_2_film_poster.jpg",
                      "https://www.youtube.com/watch?v=Ez4mXaeSKuk")
paan_singh_tomar = media.Movie("Paan Singh Tomar",
                               "The story of Paan Singh Tomar, an Indian athlete and seven-time national steeplechase champion who becomes one of the most feared dacoits in Chambal Valley after his retirement.",
                               "https://upload.wikimedia.org/wikipedia/en/9/93/Paan_Singh_Tomar_Poster.jpg",
                               "https://www.youtube.com/watch?v=EH0O75KNqkg")
#Creating a list of Objects for passing the movies object to the Fresh Tomatoes File to display
movies = [toy_story,avatar,lagaan,kahaani,paan_singh_tomar]
#Calling the funtion present in fresh_tomatoes to display the movie list and show trailer in Webbrowser
fresh_tomatoes.open_movies_page(movies)
