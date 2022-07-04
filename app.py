from auxdeck import *

data = datos_turisticos()
st.header('Elementos Turísticos Quinta Región')
st.pydeck_chart(LayeredDeck(HexTextLayers(data)))
#st.dataframe(data.groupby('ciudad').size())
st.dataframe(data.pivot_table(index='ciudad',columns='rubro',aggfunc='count',values='lat'))
st.dataframe(data)
