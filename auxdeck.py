import pydeck as pdk
from pydeck.types import String

def LayeredDeck(layers, centro = [-33.0, -71.6]):
    return pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=centro[0],longitude=centro[1],
            zoom=12,pitch=100,     controller=True,
        ),
        layers=layers, tooltip=True)
  
def Layer(layer_type, df):
  return pdk.Layer(layer_type, data=df,
            get_position='[lng, lat]',
            radius=200, elevation_scale=4, elevation_range=[0, 100],
            pickable=True, extruded=True, controller=True)

def TextLayer(df, color=[255, 0, 128]):
    return pdk.Layer("TextLayer", data=df,
    pickable=True, get_position='[lng, lat]',   # or "coordinates",
    get_text="name",    get_size=16,get_color=color,
    get_angle=0, get_text_anchor=String("middle"),
    get_alignment_baseline=String("center"))
  
def ColumnLayer(df):
    return pdk.Layer("ColumnLayer", data=df,
    get_position=["lng", "lat"],
    get_elevation="rating",
    elevation_scale=100,    radius=50,
    get_fill_color=["mrt_distance * 10", "mrt_distance", "mrt_distance * 10", 140],
    pickable=True,
    auto_highlight=True)
  
tooltip = {
    "html": "<b>{mrt_distance}</b> meters away from an MRT station, costs <b>{price_per_unit_area}</b> NTD/sqm",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}
