import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

centro = [-33.0, -71.6] # valpo!

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + centro,
    columns=['lat', 'lon'])

def Layer(layer_type, df):
  return pdk.Layer(layer_type, data=df,
            get_position='[lon, lat]',
            radius=200, elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True, extruded=True,
         )

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=centro[0],
         longitude=centro[1],
         zoom=11,
         pitch=50,
     ),
     layers=[
         Layer('HexagonLayer',df),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))
