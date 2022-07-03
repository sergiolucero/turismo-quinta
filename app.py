import numpy as np
import pandas as pd

import streamlit as st
st.set_page_config(page_title="Turismo Quinta Región", page_icon="⬇", layout="wide")
from auxdeck import *

import sqlite3
conn = sqlite3.connect('turismo.db')
sql = lambda q: pd.read_sql(q, conn)
##############################################
centro = [-33.0, -71.6] # valpo!
df = sql('SELECT * FROM datos')
#st.write('N=%d' %len(df))

colors={'Concon': [0, 255, 128], 'San Antonio': [255, 0, 128], 'Valparaiso,Chile': [255, 128, 0],}
layers = []
for city, cdf in df.groupby('ciudad'):
    layers.append(Layer('HexagonLayer',df))   # write class +=
    layers.append(TextLayer(df, colors[city]))
    layers.append(ColumnLayer(df))
st.dataframe(df.groupby('ciudad').size())
                  
#st.write('nLayers=%d' %len(layers))
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=centro[0],longitude=centro[1],
         zoom=8,pitch=50,     controller=True,
     ),
     layers=layers,

 ))

st.dataframe(df)
