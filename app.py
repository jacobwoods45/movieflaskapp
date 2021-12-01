
import search
from flask import Flask
from flask_restful import Resource, Api 




app = Flask(__name__)
api = Api(app)

class GetPlatform(Resource):
    def get(self,movie):
        returnbody = {"movie": movie,
                "platform": search.MovieSearch.dynamicSearch(movie)}
        return returnbody

class FormattedPlatform(Resource):
    def get(self, movie):
        returnbody = {"movie": movie,
                      "exact_match_bool": search.MovieSearch.doesExactExist(movie),
                        "exact_platform": search.MovieSearch.searchAllPlatforms(movie),
                        "suggestions": search.MovieSearch.searchAllPlatformsSuggestions(movie)}
        return returnbody



#test
api.add_resource(GetPlatform, '/getplatform/<string:movie>')
api.add_resource(FormattedPlatform,'/getplatformextensive/<string:movie>')
if __name__ == '__main__':
    app.run(debug=True)

