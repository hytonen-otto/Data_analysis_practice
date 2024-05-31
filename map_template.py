import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
from cartopy import crs as ccrs, geodesic as gd
import cartopy.io.img_tiles as cimgt
import shapely

plt.style.use("./styles/mystyle.mplstyle")

#Coordinates for drawing and fetching the data
name = 'EFHK'
circle_rad = 1 #km
lon = 24.9570
lat = 60.3277
xkm = 5 #Total dimension
ykm = 5 #Total dimension
zoom_lvl = 13 #Bigger=more detailed

params = namedtuple('par',['name','circe_rad','lon','lat','xkm','ykm','zoom_lvl'])
par = params(name,circle_rad,lon,lat,xkm,ykm,zoom_lvl)



def lon_kmtodeg(xkm,lat):
    return xkm/(111.320*np.cos(np.deg2rad(lat)))


def plot_closemap():
    request = cimgt.OSM() #Requesting open street map
    #request = cimgt.GoogleTiles() #Requesting google street map

    #Drawing the plot
    fig = plt.figure()
    ax = plt.subplot(projection=request.crs) #Specifying the projection
    ax.add_image(request, zoom_lvl, interpolation='spline36') #Adding the map
    ax.set_extent([lon-lon_kmtodeg(xkm,lat)/2, lon+lon_kmtodeg(xkm,lat)/2, lat-ykm/(2*110.574), lat+ykm/(2*110.574)]) #Limiting the map area (Crashs without this)
    gl = ax.gridlines(draw_labels=True,zorder=5) #Drawing grid lines
    gl.xlabel_style = {'size':14}
    gl.ylabel_style = {'size':14}
    gl.top_labels = None
    gl.right_labels = None

    #Marking the spot and drawing the scale circle
    ax.scatter(lon,lat,c='red',transform=ccrs.PlateCarree())
    ax.annotate(name,(lon+lon_kmtodeg(xkm,lat)*0.02,lat+0.02/110.574),c='red',fontsize=13,transform=ccrs.PlateCarree())
    circle_points = gd.Geodesic().circle(lon, lat, radius=circle_rad*1000)
    geom = shapely.geometry.Polygon(circle_points) #Generating the circle object
    ax.add_geometries((geom,), crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red', linewidth=2)
    ax.annotate(f'{circle_rad}km',(lon+lon_kmtodeg(circle_rad*0.7,lat),lat),c='red',fontsize=13,transform=ccrs.PlateCarree())

    ax.set_title('Esimerkki havasemakartta EFHK')
    #plt.savefig('map1.png',dpi=200)
    plt.show()

plot_closemap()
