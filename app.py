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
