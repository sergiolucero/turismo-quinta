import sqlite3, pandas as pd

conn = sqlite3.connect('turismo2.db')
sql = lambda q: pd.read_sql(q, conn)
##############################################
def datos_turisticos():
    df = sql('SELECT * FROM datos')
    df = df[[c for c in df.columns if c not in ('opening_hours')]]
    return df
