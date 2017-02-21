"""module to save instance for movies """
class Movie():
	'class movie to store data given as instance'
	def __init__(self, movie_title, movie_storyline, poster_image,
				 trailer_youtube):
		"""Inits movie class title and storyline poster-url trailer-url"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube