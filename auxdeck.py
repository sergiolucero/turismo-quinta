import pydeck as pdk
from pydeck.types import String
import streamlit as st
import seaborn as sns
import sqlite3, pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Turismo Quinta Región", 
                   page_icon="⬇", layout="wide")
#st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

tooltip = {
    "html": "<b>{name}</b> <br> rating <b>{rating}</b>/5.0 <br>Horario/Teléfono/PáginaWeb",
    "style": {"background": "steelblue", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

COLOR_KEYS = {'Concon': [0, 255, 0], 'San Antonio': [255, 0, 128], 'Valparaiso,Chile': [255, 128, 0],}
conn = sqlite3.connect('turismo2.db')
sql = lambda q: pd.read_sql(q, conn)
##############################################
def datos_turisticos():
  df = sql('SELECT * FROM datos')
  #df = pd.read_csv('turismo.csv', encoding='utf-8')
  return df

def LayeredDeck(layers, centro = [-33.0, -71.6]):
    return pdk.Deck(
        map_style='mapbox://styles/mapbox/satellite-streets-v11',
        #map_style='mapbox://styles/mapbox/light-v1',
        #explore: https://www.mapbox.com/gallery/
        #map_style=pdk.map_styles.SATELLITE,
        #map_style='mapbox://styles/mapbox/mapbox-terrain-rgb',
        initial_view_state=pdk.ViewState(
            latitude=centro[0],longitude=centro[1],
            zoom=12,pitch=100), 
        layers=layers, tooltip=tooltip)   
  
# possible layer types:  Arc, Bitmap, Column, GeoJson, GridCell,Icon, Line, Path,
# PointCloud, Polygon, Scatterplot, SolidPolygon, Text, 
# see: https://deckgl.readthedocs.io/en/latest/#gallery

def Layer(layer_type, df, color):    
    return pdk.Layer(layer_type, data=df,
                   opacity=0.8, stroked=True, filled=True,
                   radius_scale=6, radius_min_pixels=1, radius_max_pixels=100,
                   line_width_min_pixels=1,
                   get_radius="rating", 
                   get_line_color=[0, 0, 0],
                   get_position='[lng, lat]', get_fill_color=color,
                   #radius=150, elevation_scale=10, elevation_range=[0, 100],
                   pickable=True, extruded=True)

def TextLayer(df, color=[255, 0, 128]):
    return pdk.Layer("TextLayer", data=df,
    pickable=True, get_position='[lng, lat]',   # or "coordinates",
    get_text="name",    get_size=16,get_color=color,
    get_angle=0, get_text_anchor=String("middle"),
    get_alignment_baseline=String("center"))
  
def ColumnLayer(df, colorKey):
    color = COLOR_KEYS.get(colorKey, [123,0,201])
    st.write(colorKey,':',color)
    
    return pdk.Layer("ColumnLayer", data=df,
    get_position=["lng", "lat"], get_elevation="rating", elevation_scale=50,    radius=50,
    get_fill_color = color,     pickable=True,   auto_highlight=True)
###################
QUINTA_JSON = 'https://raw.githubusercontent.com/sergiolucero/turismo-quinta/main/CSV.json'
CERROS_JSON = 'https://github.com/sergiolucero/data/raw/master/GEO/cerros_de_valpo.json'

def GeoLayer(url):  
    return pdk.Layer('GeoJsonLayer', url,
                    opacity=0.8, stroked=False,
                    filled=False,extruded=True,wireframe=True,
                    get_elevation=5,
                    #get_elevation="properties.valuePerSqm / 20",
                    #get_fill_color="[255, 255, properties.growth * 255]",
                    get_line_color=[0, 255, 0], get_line_width=10)

def FullDeck(df, título):
    st.header(título)
    layers = MappedLayers(df)
    st.pydeck_chart(LayeredDeck(layers))

def MappedLayers(df):
    layers = []
    layers.append(GeoLayer(QUINTA_JSON))
    layers.append(GeoLayer(CERROS_KML))
    for city, cdf in df.groupby('ciudad'):
        color = COLOR_KEYS.get(city, [200, 20, 255])
        layers.append(Layer('ScatterplotLayer', df, color))   # write class +=
        
        layers.append(TextLayer(df, color))
        layers.append(ColumnLayer(df, city))    # makes sense?
    return layers

def Heatmap(data, título):
  st.header(título)
  pt = data.pivot_table(index='ciudad', columns='rubro', 
                      values='rating', aggfunc='mean').fillna(0)
  fig = plt.figure(figsize=(5,3))
  sns.heatmap(pt, annot=True, fmt='.2f', cmap='RdYlGn',
              annot_kws={'size':16, 'weight': 'bold'})
  st.pyplot(fig)
