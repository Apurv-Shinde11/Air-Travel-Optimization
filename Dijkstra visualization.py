import matplotlib.pyplot as plt
import networkx as nx
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Coordinates (longitude, latitude)
positions = {
    'DEL': (77.1025, 28.7041),
    'BOM': (72.8777, 19.0760),
    'BLR': (77.5946, 12.9716),
    'HYD': (78.4867, 17.3850),
    'CHN': (80.2707, 13.0827),
    'CCU': (88.3639, 22.5726),
    'AMD': (72.5714, 23.0225),
    'GOA': (74.1240, 15.2993),
    'GAU': (91.7362, 26.1445)  # Guwahati
}

edges = [
    ('DEL', 'BOM', 1140), ('DEL', 'CCU', 1300), ('DEL', 'AMD', 950), ('DEL', 'BLR', 2150), ('DEL', 'GAU', 1700),
    ('BOM', 'DEL', 1140), ('BOM', 'GOA', 580), ('BOM', 'HYD', 710), ('BOM', 'AMD', 520),
    ('BLR', 'DEL', 2150), ('BLR', 'HYD', 570), ('BLR', 'CHN', 350), ('BLR', 'GOA', 600),
    ('HYD', 'BOM', 710), ('HYD', 'BLR', 570), ('HYD', 'CHN', 630),
    ('CHN', 'BLR', 350), ('CHN', 'HYD', 630), ('CHN', 'CCU', 1370),
    ('CCU', 'DEL', 1300), ('CCU', 'CHN', 1370), ('CCU', 'GAU', 1000),
    ('AMD', 'DEL', 950), ('AMD', 'BOM', 520),
    ('GOA', 'BOM', 580), ('GOA', 'BLR', 600),
    ('GAU', 'DEL', 1700), ('GAU', 'CCU', 1000)
]

# Create directed graph
G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Create map with Cartopy
fig = plt.figure(figsize=(12, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([68, 94, 6, 37], crs=ccrs.PlateCarree())

# Add map features
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)

# Draw cities
for city, (lon, lat) in positions.items():
    ax.plot(lon, lat, 'ro', markersize=6, transform=ccrs.PlateCarree())
    ax.text(lon + 0.3, lat + 0.3, city, fontsize=10, fontweight='bold', transform=ccrs.PlateCarree())

# Draw edges
for u, v, w in edges:
    lon1, lat1 = positions[u]
    lon2, lat2 = positions[v]
    ax.plot([lon1, lon2], [lat1, lat2], color='blue', linewidth=1.2, alpha=0.7, transform=ccrs.Geodetic())

plt.title("Airline Routes Over India Map (Including Guwahati)", fontsize=16)
plt.show()