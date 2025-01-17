import os
import numpy as np
import h5py
from datetime import datetime

##############################################################
# USER DEFINE

# Set the directory paths
input_dir = '/Users/rpatnaude/Documents/MATLAB/Data/CAESAR/C130_data/'
output_dir = '/Users/rpatnaude/Documents/MATLAB/San Jose/Cirrus-Cloud Project/CAM6/Flight tracks'

project_name = 'CAESAR'

##############################################################

# Check input and output directories
if not os.path.exists(input_dir):
    raise FileNotFoundError(f"Input directory does not exist: {input_dir}")
if not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Get today's date
str_date = datetime.today().strftime('%Y-%m-%d')  # Format as yyyy-mm-dd

# Find the NetCDF files in the input directory
files = [f for f in os.listdir(input_dir) if f.endswith('.nc')]

# Initialize empty lists to store the data
TIME = []
DATE = []
LAT = []
LON = []

# Loop over files
for file in files:
    file_path = os.path.join(input_dir, file)

    try:
        with h5py.File(file_path, 'r') as f:
            time = np.array(f['Time'])
            lat = np.array(f['GGLAT'])
            lon = np.array(f['GGLON'])

            flight_date = f.attrs['FlightDate'].decode('utf-8')  # Decode if needed
            fd = flight_date.split('/')
            flt_date = int(fd[2] + fd[0] + fd[1])

            date = np.full(time.shape, flt_date)

            TIME.append(time)
            LAT.append(lat)
            LON.append(lon)
            DATE.append(date)
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        continue

# # Concatenate lists into single arrays
TIME = np.concatenate(TIME)
DATE = np.concatenate(DATE)
LAT = np.concatenate(LAT)
LON = np.concatenate(LON)

# Adjust TIME and DATE to handle cases greater than 86400 (i.e., after midnight)
for i in range(len(TIME)):
    if TIME[i] > 86400:
        TIME[i] -= 86400
        DATE[i] += 1

# Remove NaN values
nanindex = np.isnan(LAT)
DATE = DATE[~nanindex]
TIME = TIME[~nanindex]
LAT = LAT[~nanindex]
LON = LON[~nanindex]

# Sort dates to find the first and last
sorted_dates = np.sort(DATE)
first_date = sorted_dates[0]  # Earliest date
last_date = sorted_dates[-1]  # Latest date

# Convert dates to strings in YYYYMMDD format
first_date_str = str(first_date)
last_date_str = str(last_date)

# Dynamically construct the output file name
output_file = os.path.join(output_dir, f'{project_name}_track_{first_date_str}_{last_date_str}.nc')

# Create the NetCDF file and write the variables
with h5py.File(output_file, 'w') as f:
    # Create dimensions
    f.create_dataset('date', data=DATE, dtype='i4')
    f.create_dataset('time', data=TIME, dtype='i4')
    f.create_dataset('lat', data=LAT, dtype='f4')
    f.create_dataset('lon', data=LON, dtype='f4')

    # Add attributes to datasets
    f['date'].attrs['units'] = 'yyyymmdd'
    f['date'].attrs['long_name'] = 'date[yyyymmdd]'
    f['date'].attrs['_Fillvalue'] = -999
    
    f['time'].attrs['units'] = 's'
    f['time'].attrs['long_name'] = 'time of day'
    f['time'].attrs['_Fillvalue'] = -999
    
    f['lat'].attrs['units'] = 'degrees'
    f['lat'].attrs['long_name'] = 'Latitude'
    f['lat'].attrs['_Fillvalue'] = -9999.0
    
    f['lon'].attrs['units'] = 'degrees'
    f['lon'].attrs['long_name'] = 'Longitude'
    f['lon'].attrs['_Fillvalue'] = -9999.0
    
    # Global attributes
    f.attrs['creation_date'] = str_date
    f.attrs['Conventions'] = 'none'
    f.attrs['title'] = f"one column output along the {project_name} flight track (1-second interval)"