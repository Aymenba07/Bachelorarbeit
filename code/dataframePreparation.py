import contextily as ctx
import geopandas as gpd
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import pandas as pd
from sodapy import Socrata

#link : "https://raw.githubusercontent.com/greysonchung/New-York-Taxi-Data-Analysis/main/code/visualisation.ipynb"

# Example authenticated client (needed for non-public datasets):
# will be used here to avoid expected problems, while dealing 
# with our data from its source

#authentification could be used 
client = Socrata("data.cityofnewyork.us",
                  "ZSiYtf39dzKYQQwoQWlfJ4B8h",
                  username="aymen.b.aicha@gmail.com",
                  password="*Alya1312*")

def fetch_data(data:str):
    results = client.get(data, limit=1000000)
    return(results)
def preprocess_data(frame):
    df_frame = pd.DataFrame.from_records(fetch_data(frame))
    result_frame = df_frame.copy()
    #int erkennung
    result_frame["passenger_count"] = pd.to_numeric(result_frame["passenger_count"],errors='raise')
    result_frame["vendorid"] = pd.to_numeric(result_frame["vendorid"],errors='raise')
    result_frame["vendorid"] = pd.to_numeric(result_frame["vendorid"],errors='raise')
    result_frame["pulocationid"] = pd.to_numeric(result_frame["pulocationid"],errors='raise')
    result_frame["dolocationid"] = pd.to_numeric(result_frame["dolocationid"],errors='raise')
    #float erkennung
    result_frame["trip_distance"] = pd.to_numeric(result_frame["trip_distance"],errors='raise')
    result_frame["fare_amount"] = pd.to_numeric(result_frame["fare_amount"],errors='raise')
    result_frame["extra"] = pd.to_numeric(result_frame["extra"],errors='raise')
    result_frame["mta_tax"] = pd.to_numeric(result_frame["mta_tax"],errors='raise')
    result_frame["tip_amount"] = pd.to_numeric(result_frame["tip_amount"],errors='raise')
    result_frame["improvement_surcharge"] = pd.to_numeric(result_frame["improvement_surcharge"],errors='raise')
    result_frame["total_amount"] = pd.to_numeric(result_frame["total_amount"],errors='raise')
    result_frame["congestion_surcharge"] = pd.to_numeric(result_frame["congestion_surcharge"],errors='raise')
    result_frame["tolls_amount"] = pd.to_numeric(result_frame["congestion_surcharge"],errors='raise')
    if('lpep_pickup_datetime' in result_frame):
        result_frame.rename(columns={'lpep_pickup_datetime':'tpep_pickup_datetime',
        'lpep_dropoff_datetime':'tpep_dropoff_datetime'},inplace=True)
    #date erkennung
    result_frame['tpep_pickup_datetime']= pd.to_datetime(result_frame['tpep_pickup_datetime'],errors='raise')
    result_frame['tpep_dropoff_datetime']= pd.to_datetime(result_frame['tpep_dropoff_datetime'],errors='raise')

    return result_frame
