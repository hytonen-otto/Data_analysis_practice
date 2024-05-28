import matplotlib.pyplot as plt
import numpy as np
from fmiopendata.wfs import download_stored_query
import pandas as pd
from cartopy import crs as ccrs, feature as cfeature
import cartopy.io.img_tiles as cimgt

latN = 61
latS = 60
lonW = 24 
lonE = 26
cLon = 26
cLat = 65

start_time = '2024-05-25T12:20:00Z'
end_time = '2024-05-25T12:25:00Z'
 

# These both give identical results, the first one is much faster
lightning1 = download_stored_query("fmi::observations::lightning::multipointcoverage",args=["starttime=" + start_time,
                                         "endtime=" + end_time,
                                         "bbox=18,55,35,75"])
#lightning2 = download_stored_query("fmi::observations::lightning::simple")


def kmtodeg(lightning):
    help = lightning.ellipse_major[:]*1/(111.320*np.cos(lightning.latitudes[:])).clip(0.1)

    return help
'''
lightning1.latitudes  # Latitude of the lightning event [° North]
lightning1.longitudes  # Longitude of the lightning event [° East]
lightning1.times  # Time of the lightning event [datetime]
lightning1.cloud_indicator  # Indicator for cloud flashes (1 == cloud lightning)
lightning1.multiplicity  # Multiplicity of the lightning event
lightning1.peak_current  # Maximum current of the lightning event [kA]
lightning1.ellipse_major  # Location accuracy of the lightning event [km]
'''

request = cimgt.OSM() #Requesting open street map

#Kuvaajan piirto
fig1 = plt.figure(figsize=(9,5),layout="constrained")
ax = plt.subplot(projection=request.crs)
ax.add_image(request,10,interpolation='none')
ax.set_extent([lonW, lonE, latS, latN])
ax.gridlines(draw_labels=True, zorder=5) # Tämä piirtää koordinaatistoruudukon

plt.scatter(lightning1.longitudes[:], lightning1.latitudes[:], s=kmtodeg(lightning1), facecolors='none', edgecolors='r',transform=ccrs.Geodetic())
plt.title(f'Observed lightning {lightning1.times[0].date()}, {lightning1.times[0].time()}-{lightning1.times[-1].time()}')
#plt.show()
fig1.savefig('kuva2.png',dpi=500)