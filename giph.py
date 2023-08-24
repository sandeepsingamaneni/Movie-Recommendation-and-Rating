from flask import render_template
from flask.views import MethodView
import requests
import urllib.request
import json
import os

class giph(MethodView):
    def get(self):
    
     GIPHY_API_KEY = os.environ.get('GIPH_API_KEY')
     url = f'https://api.giphy.com/v1/gifs/random?api_key={GIPHY_API_KEY}&tag=movies' #api endpoint for random movie based giph
     response = requests.get(url)
     gif_data = response.json()
     gif_url = gif_data['data']['images']['original']['url']
     return render_template('giph.html', gif_url=gif_url)
