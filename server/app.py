from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://movie_user:abcd1234@localhost/movies'
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), unique=False)
    name = db.Column(db.String(80), unique=True)
    image = db.Column(db.String(250), unique=True)
    year = db.Column(db.Integer, unique=False)
    rating = db.Column(db.Float, unique=False)

    def __init__(self, country, name, image, year, rating):
        self.country = country
        self.name = name
        self.image = image
        self.year = year
        self.rating = rating
    
    def __repr__(self):
        return '<Film %r>' % self.name

@app.route('/moviesByCountry', methods=['GET'])
@cross_origin()
def filter():
    country = request.args.get('country')
    if (country == 'All'):
        movies = Movies.query.all()
        results = [
            {
                "name": movie.name,
                "year": movie.year,
                "country": movie.country,
                "image": movie.image,
                "rating": movie.rating
            } for movie in movies]

        return {"count": len(results), "movies": results}
    else:
        movies = Movies.query.filter_by(country = country).all()
        results = [
            {
                "name": movie.name,
                "year": movie.year,
                "country": movie.country,
                "image": movie.image,
                "rating": movie.rating
            } for movie in movies]

        return {"count": len(results), "movies": results}

@app.route('/getCountries', methods=['GET'])
@cross_origin()
def countries():
    countries = Movies.query.distinct(Movies.country)
    results = [country.country for country in countries]
    results.append('All')

    return {"count": len(results), "countries": results}

if __name__ == '__main__':
    app.run()