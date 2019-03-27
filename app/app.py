from flask import Flask
from bson.json_util import dumps

import service

app = Flask(__name__)

@app.route("/")
def go_home():
    return "Welcome to my Restful APP"

@app.route("/movies")
def get_movies():
    all_movies = dumps(service.get_movies())
    return all_movies

@app.route("/movies/year/<int:year>")
def get_movies_by_year(year):
    all_movies = dumps(service.get_movies_by_year(year))
    return all_movies

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)