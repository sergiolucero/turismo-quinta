import numpy as np
import pandas as pd
import pydeck as pdk
from pydeck.types import String

import streamlit as st
import sqlite3
conn = sqlite3.connect('turismo.db')
sql = lambda q: pd.read_sql(q, conn)

centro = [-33.0, -71.6] # valpo!
st.set_page_config(page_title="Turismo Quinta Región", page_icon="⬇", layout="wide")

def Layer(layer_type, df):
  return pdk.Layer(layer_type, data=df,
            get_position='[lng, lat]',
            radius=200, elevation_scale=4, elevation_range=[0, 100],
            pickable=True, extruded=True, controller=True)

def TextLayer(df):
    return pdk.Layer("TextLayer", data=df,
    pickable=True, get_position='[lng, lat]',   # or "coordinates",
    get_text="name",    get_size=16,get_color=[0, 255, 128],
    get_angle=0, get_text_anchor=String("middle"),
    get_alignment_baseline=String("center"))
  
def ColumnLayer(df):
    return pdk.Layer("ColumnLayer", data=df,
    get_position=["lng", "lat"],
    get_elevation="rating",
    elevation_scale=100,    radius=50,
    get_fill_color=["mrt_distance * 10", "mrt_distance", "mrt_distance * 10", 140],
    pickable=True,
    auto_highlight=True)
##############################################

df = sql('SELECT * FROM datos')
st.write('N=%d' %len(df))

layers = [Layer('HexagonLayer',df),  #for city, cdf in df.groupby('ciudad'),
          TextLayer(df),ColumnLayer(df),],   # was IconLayer
st.write('nLayers=%d' %len(layers))
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=centro[0],longitude=centro[1],
         zoom=8,pitch=50,
     ),
     layers=layers
 ))

st.dataframe(df)
