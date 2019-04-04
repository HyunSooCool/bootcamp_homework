import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from datetime import timedelta

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Passenger = Base.classes.passenger

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Connecting to Homepage"""
    return(

         f"Available Routes:<br/>"
         f"JSON list Precipitation:"
         f"/api/v1.0/precipitation<br/>"
         f"JSON list Stations"
         f"/api/v1.0/stations<br/>"
         f"JSON list Tempurature Observations:"
         f"/api/v1.0/tobs<br/>"
         f"It returns min/avg/max tempurature when you put Start date"
         f"/api/v1.0/<start><br/>"
         f"It returns min/avg/max tempurature between start date and end date"
         f"/api/v1.0/<start>/<end>"
         )

@app.route("/api/v1.0/precipitation")
def precipitation():

    date_prcp = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date>='2016-08-23').order_by(Measurement.date).group_by(Measurement.date).all()  
    return jsonify(date_prcp)

@app.route("/api/v1.0/stations")
def stations():

    info_statinos = session.query(Station.id, Station.station,Station.name,Station.latitude, Station.longitude, Station.elevation).all()
    return jsonify(info_statinos)

@app.route("/api/v1.0/tobs")
def tobs():

    last_year_tobs= session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= '2016-08-23').all()
    return jsonify(last_year_tobs)

@app.route("/api/v1.0/<start>")
def startDateOnly(start):
    certain_day_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    return jsonify(certain_day_temp)


@app.route("/api/v1.0/<start>/<end>")
def startDateEndDate(start,end):
    between_dates_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(between_dates_temp)

if __name__ == '__main__':
    app.run(debug=True)