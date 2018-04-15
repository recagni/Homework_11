from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import scrape_mars_solved_by_me

app = Flask(__name__)

mongo = PyMongo(app)


@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index_solved_by_me.html', mars=mars)


@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return 'Scraping Successful!'


if __name__ == "__main__":
    app.run(debug=True)
