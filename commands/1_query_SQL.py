with open("0_definitions.py") as file:
    exec(file.read())
    
#import the data to a pandas dataframe
query_string = """SET SCHEMA 'eda'; 
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
	king_county_house_sales sal ON sal.house_id = det.id;"""
df_eda = pd.read_sql(query_string, db) # read queried data from SQL database into pandas dataframe

df_eda.head(5) # look at first five lines of dataframe
df_eda.to_csv("eda1.csv")
