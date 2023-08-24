"""
A Movie Recommendation and Rating Flask app

"""

import flask
from flask.views import MethodView
from index import Index
from recommendation import recommendation
from rating import rating
from giph import giph
import os

app = flask.Flask(__name__) # our Flask app

#this is the main page when user clicks on the url
app.add_url_rule('/', 
                 view_func=Index.as_view('index'),
                 methods=['GET'])

# Movie Recommendation page
app.add_url_rule('/recommendation', 
                 view_func=recommendation.as_view('recommendation'),
                 methods=['GET'])


#this is the function which is used to get the ratings for a movie title
app.add_url_rule('/rating', 
                 view_func=rating.as_view('rating'),
                 methods=['GET'])

#this is the function which is used to get the random GIPH from a movie 
app.add_url_rule('/giph', 
                 view_func=giph.as_view('giph'),
                 methods=['GET'])

#calling the main function and setting port 8000
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8000)), host='0.0.0.0', debug=True)

