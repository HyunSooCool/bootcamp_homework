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

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

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
         f"<br/>"
         f"JSON list Precipitation: "
         f"<br/>"
         f"/api/v1.0/precipitation<br/>"
         f"<br/>"
         f"<br/>"
         f"JSON list Stations : "
         f"<br/>"
         f"/api/v1.0/stations<br/>"
         f"<br/>"
         f"<br/>"
         f"JSON list Tempurature Observations : "
         f"<br/>"
         f"/api/v1.0/tobs<br/>"
         f"<br/>"
         f"<br/>"
         f"It returns min/avg/max tempurature when you put Start date : "
         f"<br/>"
         f"/api/v1.0/start_date <-- put date! <br/>date format : yyyy-mm-dd<br/>"
         f"<br/>"
         f"<br/>"
         f"It returns min/avg/max tempurature between start date and end date : "
         f"<br/>"
         f"/api/v1.0/start_date/end_date <-- put date! <br/>date format : yyyy-mm-dd<br/>"
         )

@app.route("/api/v1.0/precipitation")
def precipitation():

    date_prcp = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date>='2016-08-23').order_by(Measurement.date).group_by(Measurement.date).all()  
    last_avg_prcp= []
    for date, avg_prcp in date_prcp:
        avg_dict = {}
        avg_dict["date"] = date
        avg_dict["avg_prcp"] = avg_prcp
        last_avg_prcp.append(avg_dict)

    return jsonify(last_avg_prcp)

@app.route("/api/v1.0/stations")
def stations():

    info_statinos = session.query(Station.id, Station.station,Station.name,Station.latitude, Station.longitude, Station.elevation).all()
    list_info_stations = []
    for id, station, name, latitude, longitude, elevation in info_statinos:
        info_station_dict ={}
        info_station_dict["id"]=id
        info_station_dict["station"] = station
        info_station_dict["name"]=name
        info_station_dict["latitude"] = latitude
        info_station_dict["longitude"]=longitude
        info_station_dict["elevation"]=elevation
        list_info_stations.append(info_station_dict)
    return jsonify(list_info_stations)

    return jsonify(info_statinos)

@app.route("/api/v1.0/tobs")
def tobs():

    last_year_tobs= session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= '2016-08-23').all()
    list_last_year_tobs = []
    for date, station, tobs in last_year_tobs:
        last_year_tobs_dict={}
        last_year_tobs_dict["date"] = date
        last_year_tobs_dict["station"] = station
        last_year_tobs_dict["tobs"] = tobs
        list_last_year_tobs.append(last_year_tobs_dict)

    return jsonify(list_last_year_tobs)

@app.route("/api/v1.0/<start>")
def startDateOnly(start):
    certain_day_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    list_days_weather = []
    for min_temp, avg_temp, max_temp in certain_day_temp:
        days_weather_dict ={}
        days_weather_dict["min_temp"] = min_temp
        days_weather_dict["avg_temp"] = avg_temp
        days_weather_dict["max_temp"] = max_temp
        list_days_weather.append(days_weather_dict)

    
    return jsonify(list_days_weather)


@app.route("/api/v1.0/<start>/<end>")
def startDateEndDate(start,end):
    between_dates_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    list_between_dates_temp = []
    for min_tobs, avg_tobs, max_tobs in between_dates_temp:
        dict_between_dates_temp = {}
        dict_between_dates_temp["min_tobs"] = min_tobs
        dict_between_dates_temp["avg_tobs"] = avg_tobs
        dict_between_dates_temp["max_tobs"] = max_tobs
        list_between_dates_temp.append(dict_between_dates_temp)
    
    return jsonify(list_between_dates_temp)

if __name__ == '__main__':
    app.run(debug=True)