import numpy as np
import pandas as pd

import streamlit as st
st.set_page_config(page_title="Turismo Quinta Región", 
                   background_color='black', page_icon="⬇", layout="wide")
from auxdeck import *

import sqlite3
conn = sqlite3.connect('turismo.db')
sql = lambda q: pd.read_sql(q, conn)
##############################################
df = sql('SELECT * FROM datos')
st.header('Elementos Turísticos Quinta Región')
st.pydeck_chart(LayeredDeck(HexTextLayers(df)))
st.dataframe(df.groupby('ciudad').size())
st.dataframe(df)
