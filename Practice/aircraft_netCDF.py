
import xarray as xr
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker
import pandas as pd
import matplotlib.dates as dates


# Import using xarray
# ds = xr.open_dataset(file)
# ds

# lat = ds.GGLAT
# lon = ds.GGLON
# #temp = np.array(ds.ATX)
# temp = np.array(ds.ATX) # temperature in kelvin
# lat = np.array(ds.GGLAT)
# lon = np.array(ds.GGLON)
# pres = np.array(ds.PSXC)
# time = np.array(ds.Time)
# alt = np.array(ds.GGALT)
# cld = np.array(ds.CONCD_RWIO)
# ice = np.array(ds.CONC2DCA_RWOI)
# wv = np.array(ds.VMR_VXL) # units in ppmv

# time = pd.to_datetime(time)

# Import with netCDF4
nc_fid = Dataset(file, 'r') 

lat = nc_fid.variables['GGLAT'][:]  # extract/copy the data
lon = nc_fid.variables['GGLON'][:]
time = nc_fid.variables['Time'][:]
temp = nc_fid.variables['ATX'][:]
pres = nc_fid.variables['PSXC'][:]
alt = nc_fid.variables['GGALT'][:]
cld = nc_fid.variables['CONCD_RWIO'][:]
ice = nc_fid.variables['CONC2DCA_RWOI'][:]


######## Plot with cartopy

plt.figure(figsize=(15,10))
fig = plt.gcf()

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([110, 170, -70, -20], crs=ccrs.PlateCarree())

ax.plot(lon,lat,color='r')
ax.coastlines()
ax.stock_img()
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
ax.text(-0.07, 0.55, 'Latitude', va='bottom', ha='center',
        rotation='vertical', rotation_mode='anchor',
        transform=ax.transAxes,fontsize = 18)
ax.text(0.5, -0.1, 'Longitude', va='bottom', ha='center',
        rotation='horizontal', rotation_mode='anchor',
        transform=ax.transAxes,fontsize=18)

cld_lat = lat[cld > 0] # Pull out lat/lon for in-cloud ice and cloud measurements
cld_lon = lon[cld > 0]
ice_lat = lat[ice > 0]
ice_lon = lon[ice > 0]

plt.figure(figsize=(15,10))
fig = plt.gcf()

##########

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([135, 150, -60, -40], crs=ccrs.PlateCarree())

ax.scatter(lon,lat,4,color='r',label='Flight track')
ax.scatter(cld_lon,cld_lat,4,color='g',label='In-cloud cloud droplets')
ax.scatter(ice_lon,ice_lat,4,color='b',label='In-cloud ice crystals')

ax.coastlines()
ax.stock_img()
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
ax.text(-0.07, 0.55, 'Latitude', va='bottom', ha='center',
        rotation='vertical', rotation_mode='anchor',
        transform=ax.transAxes,fontsize = 18)
ax.text(0.5, -0.1, 'Longitude', va='bottom', ha='center',
        rotation='horizontal', rotation_mode='anchor',
        transform=ax.transAxes,fontsize=18)

ax.legend(fontsize=12,loc='upper left')



###############


RHice = 100 * wv * 1e-6 * pres * 100 / np.exp(9.550426 - 5723.265 / (temp+273.15) + 3.53068 * np.log(temp+273.15) - 0.00728332 * (temp+273.15))
RHliq = 100 * wv * 1e-6 * pres * 100 / np.exp(54.842763 - 6763.22 / (temp+273.15) - 4.21 * np.log(temp+273.15) + 0.000367 * (temp+273.15) + \
                                              np.tanh(0.0415 * ((temp+273.15) - 218.8)) * (53.878 - 1331.22 / (temp+273.15) - 9.44523 * np.log(temp+273.15)+0.014025*(temp+273.15)))
