"""Movies data """
import media
import fresh_tomato

# Set Kung Fu Panda with title and story and poster and trailer url as instance 
Kung_Fu_Panda = media.Movie(
    'kung fo banda',
	'A big and a little clumsy Po is the biggest fan of kung fu around--which '
	'does not exactly come in handy while working every day in his family nood'
	'le shop. Unexpectedly chosen to fulfill an ancient prophecy', 
	'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220p'
	'x-Kungfupanda.jpg', 
	'https://www.youtube.com/watch?v=PXi3Mv6KMzY')
# Set Dump and dumper  title and story and poster and trailer url as instance
Wreck_It_Ralph = media.Movie(
    'Wreck-It Ralph',
	'A video game villain wants to be a hero and sets out to fulfill his dream'
	' but his quest brings havoc to the whole arcade where he lives.',
	'https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Wreckitralphposter.j'
	'peg/220px-Wreckitralphposter.jpeg', 
	'https://www.youtube.com/watch?v=87E6N7ToCxs')
# Set Monsters Inc title and story and poster and trailer url as instance
Monsters_Inc = media.Movie(
    'Monsters Inc',
    'In order to power the city, monsters have to scare children so that they '
	'scream. However, the children are toxic to the monsters',
	'https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Monsters_Inc.JPG/220'
	'px-Monsters_Inc.JPG',
	'https://www.youtube.com/watch?v=99bIX3JKkQ8')
# Set How to train your dragon title, story, poster and trailer url as instance
Your_Dragon = media.Movie(
    'How to Train Your Dragon',
	'When Hiccup and Toothless discover an ice cave that is home to hundreds o'
	'f new wild dragons and the mysterious Dragon Rider, the two friends find '
	'themselves at the center of a battle to protect the peace',
	'https://upload.wikimedia.org/wikipedia/en/thumb/9/99/How_to_Train_Your_Dr'
	'agon_Poster.jpg/220px-How_to_Train_Your_Dragon_Poster.jpg',
	'https://www.youtube.com/watch?v=oKiYuIsPxYk')
# Set Hotel transelvina title and story and poster and trailer url as instance
Hotel_Transylvania = media.Movie(
        'Hotel Transylvania',
	    'Dracula, who operates a high-end resort away from the human world, go'
		'es into overprotective mode when a boy discovers the resort and falls'
		' in love with his daughter',
		'https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/HotelTransylvani'
		'a.jpg/220px-HotelTransylvania.jpg',
		'https://www.youtube.com/watch?v=FYgzizpCTKU')
# Set Tangled title and story and poster and trailer url as instance.
Tangled = media.Movie(
    'Tangled',
	'The magically long-haired Rapunzel has spent her entire life in a tower '
	'she is about to discover the world for the first time and who she is ',
	'https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Tangled_poster.jpg/2'
	'20px-Tangled_poster.jpg',
	'https://www.youtube.com/watch?v=ip_0CFKTO9E')
# List the movies data
movie = [Your_Dragon, Monsters_Inc, Kung_Fu_Panda, Wreck_It_Ralph,
		 Hotel_Transylvania, Tangled]
# Call fresh_tomato to creat web page with parameters  movie list
fresh_tomato.open_movies_page(movie)