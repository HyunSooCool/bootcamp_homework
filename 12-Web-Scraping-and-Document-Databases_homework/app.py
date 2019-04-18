  from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_db = mongo.db.mars_db.find_one()
    return render_template("index.html", mars_db=mars_db)

@app.route("/scrape")
def scrape():
    
    mars_db=mongo.db.mars_db
    mars_data=scrape_mars.scrape_news()
    mars_data=scrape_mars.scrape_img()
    mars_data=scrape_mars.scrape_weather()
    mars_data=scrape_mars.scrape_facts()
    mars_data=scrape_mars.scrape_hemispheres()

    mars_db.update({}, mars_data, upsert=True)

    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)