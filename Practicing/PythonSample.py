#!/usr/bin/env python3
print("Hello World")

import xarray as xr

file = '/Users/rpatnaude/Documents/MATLAB/Data/CAESAR/C130_data/RF01.20240228.113900_183644.PNI.nc'
ds = xr.open_dataset(file)

