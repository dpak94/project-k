# A python program to map various cities, their location co-ordinates and their population data in India as of 2011.

# Importing required packages
import pandas as pd
import folium as fl

# Importing dataset using Pandas
df = pd.read_csv("city-coords.csv", nrows = 20) # Limiting the No. of cities to 20
print(df.columns)

# Columns of Interest  : city, lat, long, population, capital

# Defining lists for Latitude and Longitude to use loops foor multiple markers
lat_city = list(df["lat"]) # Latitude List
long_city = list(df["lng"]) # Longitude List
city_name = list(df["city"])
city_pop = list(df["population"])

# Creating Map Object using Folium
map = fl.Map(location = [20.5937, 78.9629], zoom_start = 5, tiles = "Stamen Terrain") # lat. and long. of India
fg = fl.FeatureGroup(name = "IndiaMap")


# Defining Functions

def colMarker(pop): # To assign color to city markers based on population
    if pop < 500000:
        return "yellow"
    elif pop > 500000 and pop <= 1000000:
        return "orange"
    elif pop > 1000000 and pop <= 10000000:
        return "red"
    else:
        return "pink"
   

# Creating the Markers for cities based on location using for loop
for lat, lon, c_name, pop in zip(lat_city, long_city, city_name, city_pop):
    fg.add_child(fl.CircleMarker(location = [lat, lon], radius = 6, popup = c_name + "\n" + str(pop), fill_color = colMarker(pop), color = 'grey', fill_opacity = 0.7))

# Creating geopolitical borders using GeoJson function using data from a JSON file. 
fg.add_child(fl.GeoJson(data  = open("world.json", "r", encoding = "utf-8-sig"), style_function = lambda x : {'filtercolor' : 'red' if x['properties']['POP2005'] < 10000000 
else 'orange'}))

# Saving the generated Map File 
map.add_child(fg)
map.save("popMap.html")