from auxdeck import *
import matplotlib.pyplot as plt

data = datos_turisticos()

FullDeck(data, 'Elementos Turísticos Quinta Región')
Heatmap(data, 'Estadísticas')

st.header('Datos')
st.dataframe(data)
