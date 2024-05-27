from fmiopendata.wfs import download_stored_query

composites = download_stored_query("fmi::radar::composite::dbz")


import numpy as np

composite = composites.data[-1] #For some reason, -1 is the newest and 0 is about 1h before that
# Download the image data
composite.download()
# Calibrate the data from image values to dBZ
# Calls `composite.download() if data are not already downloaded
composite.calibrate()
# Get mask for area outside the radar reach
# Calls `composite.download() if data are not already downloaded
mask1 = composite.get_area_mask()
# Get mask for invalid data
# Calls `composite.download() if data are not already downloaded
mask2 = composite.get_data_mask()
# Mask all the invalid areas using the above masks
composite.data[mask1 | mask2] = np.nan

# Plot the data for preview
import matplotlib.pyplot as plt

print(composite.time) #Composite is a radar object that has the time attribute or whatever, (time in utc)

plt.imshow(composite.data[0, :, :])
plt.show()

#Ajettavia soluja tehdään näin: #%%
#Solu ei näe ulkopuolisia asioita
#Solu ajetaan myös aina koodin ajon yhteydessä!
#Voisi käyttää esim, jos ei halua ajaa koodin raskasta osaa uudestaan!