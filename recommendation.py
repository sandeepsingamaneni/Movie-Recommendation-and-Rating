from flask import render_template
from flask.views import MethodView
from tmdbv3api import TMDb, Movie
import json
import os

class recommendation(MethodView):
    def get(self):
        tmdb = TMDb()
        tmdb.api_key = os.environ.get('TMDB_API_KEY')
        movie = Movie()
    
        popular = movie.popular() # getting popular movies from the database
    
        movies = []

        for m in popular:
          poster_path = None
          if m.poster_path:
            poster_path = f"https://image.tmdb.org/t/p/w500/{m.poster_path}"
            movies.append({
              'title':m.title,
              'overview':m.overview,
              'poster_path': poster_path
            })
        return render_template('recommendation.html' , movies=movies)
