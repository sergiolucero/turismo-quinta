from auxdeck import *
import matplotlib.pyplot as plt

data = datos_turisticos()
st.header('Elementos Turísticos Quinta Región')
st.pydeck_chart(LayeredDeck(HexTextLayers(data)))
st.header('Estadísticas')

pt = data.pivot_table(index='ciudad',columns='rubro',aggfunc='median',values='rating').fillna(0)
fig = plt.figure(figsize=(5,3))
sns.heatmap(pt, annot=True)
st.pyplot(fig)
#st.dataframe(pt)

st.header('Datos'); st.dataframe(data)
