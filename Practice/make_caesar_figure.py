import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Load the data from the CSV file
file_path = '/Users/rpatnaude/Documents/MATLAB/CSU/CAESAR/CAESAR_INPS_Table_allRF_CVI_CONC_corr_102924.csv'
INPs_table = pd.read_csv(file_path)

# Filter the data based on conditions
sdi_dat = INPs_table[(INPs_table['OFR_CVI_flag'] == 0) & (INPs_table['Conc_flag'] == 0)]
conc_dat = INPs_table[(INPs_table['OFR_CVI_flag'] == 0) & (INPs_table['Conc_flag'] == 1)]
cvi_dat = INPs_table[(INPs_table['OFR_CVI_flag'] == 1) & (INPs_table['Conc_flag'] == 0)]

# Initialize the plot
plt.figure(figsize=(12, 8))

# Define the colormap
cmap = plt.get_cmap('jet')

# Scatter plot for SDI data
scatter_sdi = plt.scatter(sdi_dat['AerT'], sdi_dat['INPs_CVI_CONC_corr_SL'], 
                            s=150, c=sdi_dat['C130_Alt_m']/1000, 
                            marker='o', edgecolor='black', cmap=cmap)

# Scatter plot for CONC data
scatter_conc = plt.scatter(conc_dat['AerT'], conc_dat['INPs_CVI_CONC_corr_SL'], 
                            s=150, c=conc_dat['C130_Alt_m']/1000, 
                            marker='s', edgecolor='black', cmap=cmap)

# Scatter plot for CVI data
scatter_cvi = plt.scatter(cvi_dat['AerT'], cvi_dat['INPs_CVI_CONC_corr_SL'], 
                            s=150, c=np.array(cvi_dat['C130_Alt_m'])/1000, 
                            marker='D', edgecolor='black', cmap=cmap)

# Adding a legend
legend = plt.legend([scatter_sdi, scatter_conc, scatter_cvi], ['ISK', 'CONC', 'CVI'], 
                    loc='best', frameon=False, ncol=3, fontsize=18)

# Adjust the marker size in the legend
for handle in legend.legend_handles:
    handle.set_sizes([12])

# Set axis labels
plt.xlabel('Temperature (°C)', fontsize=22)
plt.ylabel(r'$n_{\mathrm{INP}}$ (std L$^{-1}$)', fontsize=22)
# Set x and y limits
plt.xlim(-35, -15)
plt.ylim(0.001, 1000)

# Set x-axis ticks and labels
plt.xticks(np.arange(-35, -14, 1), 
            labels=["-35", "", "", "", "", "-30", "", "", "", "", "-25", "", "", "", "", "-20", "", "", "", "", "-15"], 
            fontsize=22)

# Set y-axis to log scale
plt.yscale('log')

# Set y-axis ticks and labels
plt.yticks([0.001, 0.01, 0.1, 1, 10, 100, 1000], 
            labels=['0.001', '0.01', '0.1', '1', '10', '100', '1000'], fontsize=22)

# Increase linewidth of the axis
plt.gca().tick_params(axis='both', width=2)

# Add colorbar
cbar = plt.colorbar(scatter_sdi, orientation='vertical',fraction=.05,pad=.03)
cbar.set_label('Altitude (km)', fontsize=20,labelpad=10)
cbar.mappable.set_clim(0, 7)
# Show the plot
plt.show()
