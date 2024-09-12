
import pandas as pd
import psycopg2



from sqlalchemy import create_engine # for creating an engine
#read the database string DB_STRING from the .env
load_dotenv()

DB_STRING = os.getenv('DB_STRING') # gets database string DB_STRING from .env file and assigns it as value for new variable DB_STRING
db = create_engine(DB_STRING) # creates engine from database string DB_STRING

import pandas as pd # if not done already

#import the data to a pandas dataframe
query_string = """
SET SCHEMA 'eda'; 
SELECT * FROM king_county_house_details;
SELECT * FROM king_county_house_sales;

SELECT
	sal.date,
	sal.price,
	sal.house_id,
	sal.id,
	det.bedrooms,
	det.bathrooms,
	det.sqft_living,
	det.sqft_lot,
	det.floors,
	det.waterfront,
	det.view,
	det.condition,
	det.grade,
	det.sqft_above,
	det.sqft_basement,
	det.yr_built,
	det.yr_renovated,
	det.zipcode,
	det.lat,
	det.long,
	det.sqft_living15,
	det.sqft_lot15         
FROM 
	king_county_house_details det 
INNER JOIN 
	king_county_house_sales sal ON sal.house_id = det.id;

"""

df_sqlalchemy = pd.read_sql(end_data, db) # read queried data from SQL database into pandas dataframe
df_sqlalchemy.head(30) # look at first five lines of dataframe