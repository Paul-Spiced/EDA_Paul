# Setting packages
import pandas as pd
import psycopg2
from sqlalchemy import create_engine # for creating an engine
import os
from dotenv import load_dotenv # reads key-value pairs from a .env file and can set them as environment variables
#read the database string DB_STRING from the .env

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# Setting the colors 
def pr_col(text, color, end='\n'):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get(color, '') + text + reset + end)

# Importing the 'os' module for operating system-dependent functionality
import os


# settings for query from SQL 
load_dotenv()
DB_STRING = os.getenv('DB_STRING') # gets database string DB_STRING from .env file and assigns it as value for new variable DB_STRING
db = create_engine(DB_STRING) # creates engine from database string DB_STRING



# Variable in question: 
def num_question_f():
    num_question = [
	'bedrooms_to_sqliving',
	'bethrooms_to_sqliving',
    'price'  ]
    return num_question

# print(numeric_in_question_f ())
 

def numerical_f():
    numerical_features = [
	'price',
	'sqft_living',
	'sqft_lot',
	'sqft_above',
	'sqft_basement',
	'yr_built',
	'yr_renovated',
	'lat',
	'long',
	'sqft_living15',
	'sqft_lot15'   ]
    return numerical_features

# print(numerical_f())

def categorical_f():
    categorical_features = [
	'bedrooms' , 
    'zipcode',
	'bathrooms' , 
	'floors' , 
	'waterfront' , 
	'view' , 
	'condition' ,     
	'grade'  ]
    return categorical_features

# print(categorical_f ())