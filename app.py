from auxdeck import *
import matplotlib.pyplot as plt

data = datos_turisticos()
st.header('Elementos Turísticos Quinta Región')
st.pydeck_chart(LayeredDeck(HexTextLayers(data)))
st.header('Estadísticas')

pt = data.pivot_table(index='ciudad', columns='rubro', 
                      values='rating', aggfunc='mean').fillna(0)
fig = plt.figure(figsize=(5,3))
sns.heatmap(pt, annot=True, fmt='.2f', cmap='RdYlGn',
            annot_kws={'size':16, 'weight': 'bold'})
st.pyplot(fig)
#st.dataframe(pt)

st.header('Datos'); st.dataframe(data)
