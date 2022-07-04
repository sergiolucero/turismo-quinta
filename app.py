from auxdeck import *

data = datos_turisticos()
st.header('Elementos Turísticos Quinta Región')
st.pydeck_chart(LayeredDeck(HexTextLayers(data)))
st.header('Estadísticas')
st.dataframe(data.pivot_table(index='ciudad',columns='rubro',aggfunc='count',values='lat').fillna(0))
st.header('Datos'); st.dataframe(data)
