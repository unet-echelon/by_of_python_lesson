# movie = 'The good, the bad, adn the ugly'

# rating = 100
# resault = f'Movie: "{movie}", rating: {rating}'

# print(resault)


# movie = 'Alien'
# rating = 200

# resault = f'Movie: "{movie}", rating: {rating}'

# print(resault)

greeting = 'Hello'
to = "World"

def greet(message, name):
	# print('Hello', name)
	resault = f'{message}, {name}'
	# print(resault)
	return resault
g = greet(greeting, to).title()
print(g)



def movies(movie, rating):
	resault = f'Movie: {movie}, rating: {rating}'
	return resault

ss = movies("alien", "254")
print(ss)
