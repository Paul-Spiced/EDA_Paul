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



load_dotenv()

DB_STRING = os.getenv('DB_STRING') # gets database string DB_STRING from .env file and assigns it as value for new variable DB_STRING
db = create_engine(DB_STRING) # creates engine from database string DB_STRING

import pandas as pd # if not done already

