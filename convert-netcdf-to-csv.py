import os
import pandas as pd
import netCDF4
from netCDF4 import Dataset

def load_cdf_file_as_dataframe(file):
    nc = netCDF4.Dataset(file)
    
    sst = nc.variables['sea_surface_temperature'][0].data
    lat = nc.variables['lat'][:].data
    lon = nc.variables['lon'][:].data
    
    # collect column names in a dictionary
    d = {}
    for col in lon[:].data:
        d[col] = []
        
    # create dataframe using dictionary
    df = pd.DataFrame(d)
    
    # insert rows of sea surface temperature into dataframe
    for i, row_index in enumerate(lat[:].data):
        df.loc[i] = sst[i]
        
    # set each row's index as its corresponding latitude
    df.index = lat[:].data
    
    return df

nc_file = './data/20160702134026-NCEI-L3C_GHRSST-SSTskin-AVHRR_Pathfinder-PFV5.3_NOAA19_G_2016184_day-v02.0-fv01.0.nc'
print('Converting netcdf file to csv. This will take a few minutes...')
df = load_cdf_file_as_dataframe(nc_file)
print('Conversion completed')

csv_file = './data_processed/20160702134026_data.csv'
print(f'Saving csv file to: {csv_file}')
df.to_csv(csv_file)