import matplotlib.pyplot as plt
import numpy as np
from fmiopendata.wfs import download_stored_query
from cartopy import crs as ccrs, geodesic as gd
import cartopy.io.img_tiles as cimgt
import shapely

#Coordinates for drawing and fetching the data
latN = 61
latS = 60
lonW = 24 
lonE = 26

#Time window for the data
start_time = '2024-05-25T12:20:00Z'
end_time = '2024-05-25T12:21:00Z'
 
#Fetching the data
lightning1 = download_stored_query("fmi::observations::lightning::multipointcoverage",args=["starttime=" + start_time,
                                         "endtime=" + end_time,f"bbox={lonW},{lonE},{latS},{latN}"])

print('Salamoiden lukumäärä: ', len(lightning1.times))
print('Pienin virheraja (km): ', min(lightning1.ellipse_major))
print('Suurin virheraja (km): ', max(lightning1.ellipse_major))
print('Keskimääräinen virheraja (km): ', np.average(lightning1.ellipse_major))


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

#Drawing the plot
fig1 = plt.figure(figsize=(9,5),layout="constrained")
ax = plt.subplot(projection=request.crs) #Specifying the projection
ax.add_image(request,10,interpolation='none') #Adding the map
ax.set_extent([lonW, lonE, latS, latN]) #Limiting the map area (Crashs without this)
ax.gridlines(draw_labels=True, zorder=5) #Drawing grid lines

#Drawing the circles centered at the lightning location, radius is the accuracy of the event
for i in range(len(lightning1.times)):
    circle_points = gd.Geodesic().circle(lon=lightning1.longitudes[i], lat=lightning1.latitudes[i], radius=lightning1.ellipse_major[i]*1000)
    geom = shapely.geometry.Polygon(circle_points) #Generating the circle object
    ax.add_geometries((geom,), crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red', linewidth=1) 
    #Adding circles to map, NOTICE the projection transformation (the data is in PlateCarree format)

plt.title(f'Observed lightning {lightning1.times[0].date()}, {lightning1.times[0].time()}-{lightning1.times[-1].time()}')
plt.show()
#fig1.savefig('kuva1.png',dpi=500)