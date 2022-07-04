import pydeck as pdk
from pydeck.types import String
import streamlit as st
import sqlite3, pandas as pd

st.set_page_config(page_title="Turismo Quinta Región", 
                   page_icon="⬇", layout="wide")
#st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

tooltip = {
    "html": "<b>{name}</b> <br> rating <b>{rating}</b>/5.0 <br>Horario/Teléfono/PáginaWeb",
    "style": {"background": "steelblue", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

colors={'Concon': [0, 255, 0], 'San Antonio': [255, 0, 128], 'Valparaiso,Chile': [255, 128, 0],}
conn = sqlite3.connect('turismo.db')
sql = lambda q: pd.read_sql(q, conn)
##############################################
def datos_turisticos():
  df = sql('SELECT * FROM datos')
  return df

def LayeredDeck(layers, centro = [-33.0, -71.6]):
    return pdk.Deck(
        #map_style='mapbox://styles/mapbox/satellite-streets-v11',
        map_style='mapbox://styles/mapbox/light-v1',
        #explore: https://www.mapbox.com/gallery/
        #map_style=pdk.map_styles.SATELLITE,
        #map_style='mapbox://styles/mapbox/mapbox-terrain-rgb',
        initial_view_state=pdk.ViewState(
            latitude=centro[0],longitude=centro[1],
            zoom=12,pitch=100,
        ), 
        layers=layers, tooltip=tooltip)   # controller=True???
  
# possible layer types:  Arc, Bitmap, Column, GeoJson, GridCell,Icon, Line, Path,
# PointCloud, Polygon, Scatterplot, SolidPolygon, Text, 
# see: https://deckgl.readthedocs.io/en/latest/#gallery

def Layer(layer_type, df, color):
  return pdk.Layer(layer_type, data=df,
                   opacity=0.8, stroked=True, filled=True,
                   radius_scale=6, radius_min_pixels=1, radius_max_pixels=100,
                   line_width_min_pixels=1,
                   get_radius="rating", #"exits_radius",
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
  
def ColumnLayer(df):
    return pdk.Layer("ColumnLayer", data=df,
    get_position=["lng", "lat"], get_elevation="rating", elevation_scale=100,    radius=50,
    get_fill_color=["mrt_distance * 10", "mrt_distance", "mrt_distance * 10", 140],   # FIX THIS
    pickable=True,   auto_highlight=True)

import json
def GeoLayer(filename):
    js = json.load(open(filename).read())    
    return pdk.Layer('GeoJsonLayer', js)
  
def HexTextLayers(df):
    layers = []
    for city, cdf in df.groupby('ciudad'):
        layers.append(Layer('ScatterplotLayer',df, colors[city]))   # write class +=
        layers.append(TextLayer(df, colors[city]))
        #layers.append(ColumnLayer(df))
    return layers
