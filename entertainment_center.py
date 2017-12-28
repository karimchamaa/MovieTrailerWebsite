import media
import fresh_tomatoes

#Twenty_One Movie
twenty_one_title = "21"
twenty_one_image = "https://upload.wikimedia.org/wikipedia/en/a/a8/21_%282008_film%29.jpg"
twenty_one_trailer = "https://www.youtube.com/watch?v=26vEcvI3v-Y"
twenty_one = media.Movie(twenty_one_title, twenty_one_image, twenty_one_trailer)

#Braveheart Movie
braveheart_title = "Braveheart"
braveheart_image = "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg"
braveheart_trailer = "https://www.youtube.com/watch?v=wj0I8xVTV18"
braveheart = media.Movie(braveheart_title, braveheart_image, braveheart_trailer)

#Titanic Movie
titanic_title = "Titanic"
titanic_image = "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg"
titanic_trailer = "https://www.youtube.com/watch?v=2e-eXJ6HgkQ"
titanic = media.Movie(titanic_title, titanic_image, titanic_trailer)

#Escape from Alcatraz Movie
escape_alcatraz_title = "Escape from Alcatraz"
escape_alcatraz_image = "https://upload.wikimedia.org/wikipedia/en/0/0d/Escape_from_alcatraz.jpg"
escape_alcatraz_trailer = "https://www.youtube.com/watch?v=KSS0fH9zzFY"
escape_alcatraz = media.Movie(escape_alcatraz_title, escape_alcatraz_image, escape_alcatraz_trailer)

movies = [twenty_one, braveheart, titanic, escape_alcatraz]
fresh_tomatoes.open_movies_page(movies)
