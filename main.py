# print("Hello World")

import xarray as xr
import numpy as np

file = "/Users/rpatnaude/Documents/MATLAB/Data/CAESAR/C130_data/RF01.20240228.113900_183644.PNI.nc"
ds = xr.open_dataset(file,engine="netcdf4")

#Find median and std for o3 and ps

#ds = xr.open_dataset('MERRA2_400.inst3_3d_chm_Nv.20170101.nc4')
wic = np.array(ds.WIC[:]) # This will pull the variable, and only use the surface level
# ps = np.array(ds.PS)
# t_sfc = np.array(ds['T'][:,0,:,:]) # same as above

# med_ps = np.median(ps)
# std_ps = np.std(ps)
# med_o3 = np.nanmedian(o3_sfc)
# std_o3 = np.nanstd(o3_sfc)