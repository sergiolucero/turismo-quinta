import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

centro = [-33.0, -71.6] # valpo!

def data(ciudad):
    #URL = 'http://quant.cl/places/Vi%C3%B1a%20del%20mar_mariscos'
    if ciudad == 'Valparaiso':
        df = pd.read_csv('Valpo.csv')
    else:
        URL = 'http://quant.cl/places/%s_mariscos' %ciudad
        df = pd.read_html(URL)[0]
    
    df = df[['lat','lng']]  # removes latin-1 problems!
    return df

def Layer(layer_type, df):
  return pdk.Layer(layer_type, data=df,
            get_position='[lat, lng]',
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

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=centro[0],longitude=centro[1],
         zoom=11,pitch=50,
     ),
     layers=[Layer('HexagonLayer',df)     ],
 ))

st.dataframe(df)
