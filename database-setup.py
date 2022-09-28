import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup           
#################################################
##### MAKE SURE TO CHANGE 'password' TO YOUR PASSWORD
engine = create_engine("postgresql://postgres:sydney20@localhost/groupcv2.ci6szv7owa4r.us-east-1.rds.amazonaws.com\
")

# Create Table
engine.execute('CREATE TABLE IF NOT EXISTS ds_salariesv1 \
work_year varchar(255), \
experience_level varchar(255), \
employment_type varchar(255), \
job_title varchar(255), \
salary varchar(255), \
salary_currency varchar(255), \
salary_in_usd varchar(255), \
employee_residence varchar(255), \
remote_ratio varchar(255), \
company_location varchar(255), \
company_size varchar(255)) \
')

# insert data (CSV's)
engine.execute("COPY ds_salariesv1 FROM 'C:/Users/bassm/Desktop/GitHub Repository/Project3-GroupC/Resources/ds_salariesv1.csv' WITH (FORMAT csv);")

# C:/Users/bassm/Desktop/GitHub Repository/Project3-GroupC/Resources/ds_salariesv1.csv

