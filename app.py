
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
#test
api.add_resource(GetPlatform, '/getplatform/<string:movie>')
if __name__ == '__main__':
    app.run(debug=True)

