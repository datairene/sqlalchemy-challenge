# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
import datetime as dt
import numpy as np

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route('/')
def welcome():
    return(
        f"Welcome!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MM/DD/YYYY.</p>" 
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    """Return the precipitation for the last year"""
     # Calculate the date 1 year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

     #Query data for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()
    session.close()

     #Dictionary Comprehension
    precip = (date: prcp for date, prcp in precipitation)
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations();
     result = session.query(Station.station).all()
     session.close()
     station = list(np.ravel(result))
     return jsonify(stations = station)

@app.route('/api/v1.0/tobs')
def tobs();
     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
     result = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
     
     session.close()

     temps = list(np.ravel(result))

     return jsonify(temps = temps)

@app.route("/api/v1.0/start")
@app.route("/api/v1.0/start/end")
def stats(start, end=None):
     #select statement
     sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
     start = dt.datetime.strptime(start, "%m%d%Y")
     if not end:
         results = session.query(*sel).\
            filter(Measurement.date >= start).all()
         
         session.close()

         temps = list(np.ravel(result))
         return jsonify(tobs_stats = tobs_stats)
     
     end = dt.datetime.strptime(end, "%m%d%Y")
     results = session.query(*sel).\
     filter(Measurement.date >= start).\
     filter(Measurement.date <= end).all()
         
     session.close()

     temps = list(np.ravel(result))
     return jsonify(tobs_stats = tobs_stats)
 if __name__ == '__main__':
    app.run()

