from pymongo import MongoClient

client = MongoClient()

db = client.get_database(name="imdb")

movies = db.get_collection("movies")

print ("Counter: {}".format(movies))

def get_movies():
    return movies.find()

def get_movies_by_year(year):
    return movies.find({ 'year': year })