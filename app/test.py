import service
from pprint import pprint

all_movies = service.get_movies()

service.get_movies()

response_movies = []

print("Displaying movies: {}\n".format(type(all_movies)))
for movie in all_movies:
    # print("Title: {}".format(movie['title']))
    response_movies.append(movie)
    # pprint(movie)

print("\n\nFinished!")