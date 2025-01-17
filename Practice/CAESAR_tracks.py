# print("Hello World")
import cartopy
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import os
from itertools import cycle
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

###########
input_dir = '/Users/rpatnaude/Documents/MATLAB/Data/CAESAR/C130_data/'
files = [f for f in os.listdir(input_dir) if f.endswith('.nc')]

# Create the figure and axes outside the loop
plt.figure(figsize=(8, 8))
ax = plt.axes(projection=ccrs.NorthPolarStereo())
ax.set_extent([-90, 90, 90, 56], crs=ccrs.PlateCarree())
ax.gridlines()
ax.add_feature(cartopy.feature.LAND, edgecolor='black', zorder=1)

# Define a list of colors
colors = ['r', 'b', 'g', 'm', 'c', 'y', 'k']  # Add more colors if needed
color_cycle = cycle(colors)  # Create a cyclic iterator

# Iterate through files and plot each track
for idx, file in enumerate(files, start=1):  # Start index from 1
    file_path = os.path.join(input_dir, file)
    
    # Import with xarray
    ds = xr.open_dataset(file_path, engine="netcdf4")
    lat = np.array(ds.GGLAT)
    lon = np.array(ds.GGLON)

    color = next(color_cycle)
    # Plot each track
    label = f'RF{idx:02d}'  # Zero-padded index, e.g., RF01, RF02, etc.
    plt.plot(
        lon, lat,
        color=color, transform=ccrs.PlateCarree(),
        label=label, zorder=5
    )

ax.legend(fontsize='x-large')

plt.show()
    
# print(lat)