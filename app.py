import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

centro = [-33.0, -71.6] # valpo!

def Layer(layer_type, df):
  return pdk.Layer(layer_type, data=df,
            get_position='[lng, lat]',
            radius=200, elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True, extruded=True,
         )
##############################################
import sqlite3
conn = sqlite3.connect('turismo.db')
sql = lambda q: pd.read_sql(q, conn)
df = sql('SELECT * FROM datos')
st.write('N=%d' %len(df))

layers = [Layer('IconLayer',cdf)  for city, cdf in df.groupby('ciudad') ],   # was HexagonLayer
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
