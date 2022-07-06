import sqlite3, pandas as pd
import streamlit as st

conn = sqlite3.connect('turismo2.db')
sql = lambda q: pd.read_sql(q, conn)
##############################################
@st.experimental_memo
def datos_turisticos():
    df = sql('SELECT * FROM datos')
    df = df[[c for c in df.columns if c not in ('opening_hours')]]
    return df
