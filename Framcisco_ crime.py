import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from IPython.display import display
import folium
import squarify
from IPython.core.display import HTML


#Choropleth map to visualize crime in San Francisco
# read the data csv file 

data= pd.read_csv("https://cocl.us/sanfran_crime_dataset",index_col=0)
pd.options.display.max_columns = None 
data.isnull().sum()
print(data.columns)
print(data.head(10))
t= data.PdDistrict.value_counts()
df_crime1= pd.DataFrame(data= t.values, index= t.index,columns= ['Count'])
df_crime1 = df_crime1.reindex(["CENTRAL", "NORTHERN", "PARK",
                               "SOUTHERN", "MISSION", "TENDERLOIN", "RICHMOND", 
                               "TARAVAL", "INGLESIDE", "BAYVIEW"])
df_crime1 = df_crime1.reset_index()
df_crime1.rename({'index':'Neighborhood'}, axis ='columns', inplace=True)
print(df_crime1)


gjson = 'https://cocl.us/sanfran_geojson'
map = folium.Map(location = [37.77, -122.42], zoom_start = 12)
HTML(map._repr_html_())
#generate map
map.choropleth(geo_data= gjson, data= df_crime1, columns= ['Neighborhood', 'Count'], key_on= 'feature.properties.DISTRICT', fill_color= 'YlOrRd', fill_opacity= 0.7, line_opacity= 0.2, legend_name= 'Crime Rate in San Francisco')
display(map)









