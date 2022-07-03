import numpy as np
import pandas as pd

import streamlit as st
st.set_page_config(page_title="Turismo Quinta Región", page_icon="⬇", layout="wide")
from auxdeck import *

import sqlite3
conn = sqlite3.connect('turismo.db')
sql = lambda q: pd.read_sql(q, conn)
##############################################
st.header('Elementos Turísticos Quinta Región')
df = sql('SELECT * FROM datos')
#st.write('N=%d' %len(df))

colors={'Concon': [0, 255, 128], 'San Antonio': [255, 0, 128], 'Valparaiso,Chile': [255, 128, 0],}
layers = []
for city, cdf in df.groupby('ciudad'):
    layers.append(Layer('HexagonLayer',df))   # write class +=
    layers.append(TextLayer(df, colors[city]))
    layers.append(ColumnLayer(df))
                  
#st.write('nLayers=%d' %len(layers))
st.pydeck_chart(LayeredDeck(layers))
st.dataframe(df.groupby('ciudad').size()T)

st.dataframe(df)
