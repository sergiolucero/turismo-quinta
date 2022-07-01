import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

centro = [-33.0, -71.6] # valpo!

def data(ciudad):
    #URL = 'http://quant.cl/places/Vi%C3%B1a%20del%20mar_mariscos'
    #URL = 'http://quant.cl/places/%s_mariscos' %ciudad
    #df = pd.read_html(URL)[0]
    df = pd.read_csv('Valpo.csv')
    #df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + centro,    columns=['lat', 'lon'])
    df = df[['lat','lng']]  # removes latin-1 problems!
    return df

def Layer(layer_type, df):
  return pdk.Layer(layer_type, data=df,
            get_position='[lng, lat]',
            radius=200, elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True, extruded=True,
         )
##############################################
df = data('Valpo')
st.write('N=%d' %len(df))

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=centro[0],longitude=centro[1],
         zoom=11,pitch=50,
     ),
     layers=[
         Layer('HexagonLayer',df),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lng, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))

st.dataframe(df)
