from auxdeck import *
import matplotlib.pyplot as plt

data = datos_turisticos()

st.header('Elementos Turísticos Quinta Región')
st.pydeck_chart(LayeredDeck(HexTextLayers(data)))

st.header('Estadísticas')
Heatmap(data)

st.header('Datos')
st.dataframe(data)
