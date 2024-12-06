# print("Hello World")
import cartopy
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

###########
fid = "/Users/rpatnaude/Documents/MATLAB/Data/CAESAR/C130_data/RF01.20240228.113900_183644.PNI.nc"

# Import with xarray
# ds = xr.open_dataset(fid,engine="netcdf4")
# lat = np.array(ds.GGLAT)
# lon = np.array(ds.GGLON)

# import with netCDF4
nc_fid = Dataset(fid, 'r') 
lat = nc_fid.variables['GGLAT'][:]  # extract/copy the data
lon = nc_fid.variables['GGLON'][:]

#Find median and std for o3 and ps

#ds = xr.open_dataset('MERRA2_400.inst3_3d_chm_Nv.20170101.nc4')
# wic = np.array(ds.WIC) # This will pull the variable, and only use the surface level
# time = np.array(ds.Time)

# ps = np.array(ds.PS)

plt.figure(figsize=(8,8))

fig = plt.gcf()
# 
ax = plt.axes(projection=ccrs.NorthPolarStereo())
# ax.set_extent([-20, 30, 86, 55], crs=ccrs.PlateCarree())

plt.plot(lon,lat,color='r',transform=ccrs.PlateCarree(),label='C130 track',zorder=5)
# ax.coastlines()
# ax.stock_img()
ax.gridlines()
ax.legend(fontsize='x-large')
ax.set_extent([-180, 180, 90, 56], ccrs.PlateCarree())

ax.add_feature(cartopy.feature.LAND, edgecolor='black',zorder=1)

# ax.legend(fontsize='x-large')

# gl = ax.gridlines(crs=ccrs.NorthPolarStereo(), draw_labels=True,
#                   linewidth=2, color='gray', alpha=0.5, linestyle='--')
# gl.xlabels_top = False
# gl.ylabels_right = False
# gl.xformatter = LONGITUDE_FORMATTER
# gl.yformatter = LATITUDE_FORMATTER
# ax.text(-0.07, 0.55, 'Latitude', va='bottom', ha='center',
#         rotation='vertical', rotation_mode='anchor',
#         transform=ax.transAxes,fontsize = 18)
# ax.text(0.5, -0.1, 'Longitude', va='bottom', ha='center',
#         rotation='horizontal', rotation_mode='anchor',
#         transform=ax.transAxes,fontsize=18)

plt.show()
    
# print(lat)