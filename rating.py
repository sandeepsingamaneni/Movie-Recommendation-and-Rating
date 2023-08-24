from flask import render_template, request
from flask.views import MethodView
from imdb import IMDb
import json
import os

class rating(MethodView):
 def get(self):
    imdb = IMDb() # create imdb API object
    title = request.args.get("title") # Get the value of title input from the form
    results = imdb.search_movie(title)
    movies = []

    for i in results:
        movie = imdb.get_movie(i.movieID)
        if 'rating' in movie.data:
            rating = movie['rating']
        else:
            rating = "N/A"

        description = movie.get('plot', '')    
        movies.append({'title': movie['title'], 'rating': rating, 'description': description})

    return render_template('rating.html' , movies=movies)
 
