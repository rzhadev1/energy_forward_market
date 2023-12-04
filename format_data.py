import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt

PTH = '/Users/richardz/Desktop/Projects/energy_forward_market/data'
LOAD_FILE = 'load_2021.xlsx'
DAM_PRICES_FILE = 'dam_spp_2021.xlsx'
RENEW_FILE = 'wind_solar_2021.xlsx'

# get the historical load data for a specific zone
def get_load(zone): 
	pass

# get the average price of all hubs in ERCOT
def get_dam_prices(zone='HB_BUSAVG'): 
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
	df = pd.DataFrame()
	for month in months: 
		dam_prices = pd.read_excel(os.path.join(PTH, DAM_PRICES_FILE), sheet_name=month)
		dam_prices = dam_prices[dam_prices['Settlement Point'] == zone]
		df = pd.concat([df, dam_prices], axis=0)
		
	return df	

# get the wind and solar data
def get_wind_solar(): 
	wind_sheet = 'Wind Data'
	solar_sheet = 'Solar Data'
	wind_data = pd.read_excel(os.path.join(PTH, RENEW_FILE), sheet_name=wind_sheet)
	solar_data = pd.read_excel(os.path.join(PTH, RENEW_FILE), sheet_name=solar_sheet)
	return wind_data, solar_data

