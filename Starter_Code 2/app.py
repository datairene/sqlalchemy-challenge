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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        f"Routes:<br/>"
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Calculate the date 1 year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    #Query data for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()
    session.close()

    #Dictionary Comprehension
    precip = (date: prcp for date, prcp is precipitation)
    return jsonify(precip)

@app.route('/api/v1.0/precipitation')
def stations()

if __name__ == '__main__':
    app.run()