import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('india_map_project_data.csv')

list_of_state = list(df['State'].unique())
list_of_state.insert(0,'overall India')

st.sidebar.title('India Data Visualization Project')

selected_state = st.sidebar.selectbox('Select a state',list_of_state)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[6:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[6:]))

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size represent primary parameter')
    st.text('Color represent secondary parameter')
    if selected_state == 'overall India':
        #plot for india
        fig = px.scatter_mapbox(df, lat = 'Latitude', lon = 'Longitude',
                                mapbox_style = 'carto-positron',
                                size=primary, color=secondary,
                                zoom=3, size_max=30,
                                width = 1000 ,height = 700,
                                hover_name = 'District'
                                 )
        st.plotly_chart(fig, use_cintainer_width = True)
    else:
        #plot for state
        state_df = df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',
                                mapbox_style='carto-positron',
                                size=primary, color=secondary,
                                zoom=3, size_max=30,
                                width=1000, height=700,
                                hover_name='District'
                                )
        st.plotly_chart(fig, use_cintainer_width=True)


