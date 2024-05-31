import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs, geodesic as gd
import cartopy.io.img_tiles as cimgt
import shapely

plt.style.use("./styles/mystyle.mplstyle")

#Coordinates for drawing and fetching the data
name = 'EFHK'
circle_rad = 5 #km
lon = 24.9570
lat = 60.3277
xkm = 20 #Total dimension
ykm = 20 #Total dimension
zoom_lvl = 10 #Bigger=more detailed


def kmtodeg(xkm,lat):
    return xkm/(111.320*np.cos(np.deg2rad(lat)))

#request = cimgt.OSM() #Requesting open street map
request = cimgt.GoogleTiles() #Requesting google street map

#Drawing the plot
fig1 = plt.figure(layout="constrained")
ax = plt.subplot(projection=request.crs) #Specifying the projection
ax.add_image(request, zoom_lvl, interpolation='spline36') #Adding the map
ax.set_extent([lon-kmtodeg(xkm,lat)/2, lon+kmtodeg(xkm,lat)/2, lat-ykm/(2*110.574), lat+ykm/(2*110.574)]) #Limiting the map area (Crashs without this)
gl = ax.gridlines(draw_labels=True, zorder=5) #Drawing grid lines
gl.xlabel_style = {'size':14}
gl.ylabel_style = {'size':14}
#Marking the spot and drawing the scale circle
ax.scatter(lon,lat,c='red',transform=ccrs.PlateCarree())
ax.annotate(name,(lon+0.003,lat+0.003),c='red',fontsize=13,transform=ccrs.PlateCarree())
circle_points = gd.Geodesic().circle(lon, lat, radius=circle_rad*1000)
geom = shapely.geometry.Polygon(circle_points) #Generating the circle object
ax.add_geometries((geom,), crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red', linewidth=1)
ax.annotate(f'{circle_rad}km',(lon+kmtodeg(circle_rad,lat)-0.03,lat),c='red',fontsize=13,transform=ccrs.PlateCarree())

ax.set_title('Esimerkki havasemakartta EFHK')
#plt.savefig('map1.png',dpi=200)
plt.show()