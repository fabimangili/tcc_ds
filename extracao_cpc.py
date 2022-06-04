# Autor: Fabiana Bezerra Mangili
# Date: 23/03/2022

import pandas as pd
import xarray as xr
import csv

def extract (variavel):
    with open('coord_cpc.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            ds = xr.open_mfdataset(variavel+'/*.nc')
            dsloc = ds.sel(lon=float(row[1]), lat=float(row[2]), method='nearest')
            var, time = dsloc[variavel].values, dsloc['time'].values
            tempo = pd.DataFrame(var, time)
            exp_csv = tempo.to_csv('extraido_50/' + variavel + str(row[0]) + '.csv', header=False)

#extract('tmax') #tmin #tmax #precip


