import streamlit as st
import pandas as pd
import numpy as np

from controller import AppController

region_map = {
    'Distrito': 'District',
    'Barrio': 'Neighborhood'
}
controller = AppController('HandsOn/Group21/rdf/200342-0-centros-dia-with-links.ttl')

st.title('Centros de Día para Adultos Mayores en Madrid')

total, accessibility = controller.get_total_centers_and_accessibility()
total_centers_col, accessibility_col = st.columns(2)
total_centers_col.metric("Total de Centros", total)
accessibility_col.metric("Accesibilidad", f'{accessibility}%')

region_tab, subway_tab = st.tabs(
    ['Análisis por región', 'Accesibilidad por metro'])

with region_tab:
    option = st.selectbox(
        'Región a analizar',
        ['Distrito', 'Barrio'],
    )
    region = region_map[option]
    region_options = controller.get_regions(region)

    st.subheader(f'Número de centros por {option.lower()}')
    number_centers_by = controller.get_center_counts(region)
    st.bar_chart(number_centers_by)

    st.subheader(f'Mapa de los centros por {option.lower()}')
    settlement_name = st.select_slider(
        f'Seleccione el {option.lower()} a visualizar',
        region_options
    )

    map_col, info_col = st.columns(2)
    with st.spinner('Cargando...'):
        centers_data = controller.get_center_locations_by_region(settlement_name, region)
        map_col.map(centers_data)
        info_col.dataframe(centers_data.drop(['lat', 'lon'], axis=1), use_container_width=True)

with subway_tab:
    subways_options = controller.get_subway_stops()

    st.subheader(f'Mapa de los centros cerca de las estaciones de metro')
    subway_name = st.select_slider(
        f'Seleccione la estación de metro a visualizar',
        subways_options
    )

    subway_info_col, subway_map_col = st.columns(2)
    centers_by_subway_data = controller.get_centers_by_subway_stop(subway_name)
    subway_map_col.map(centers_by_subway_data)

    subway_info_col.metric(
        'Cantidad de centros cerca',
        centers_by_subway_data.shape[0])
    subway_info_col.dataframe(
        centers_by_subway_data.drop(['lat', 'lon'], axis=1),
        use_container_width=True)

    st.subheader(f'Mapa de los centros por cantidad de estaciones de metro cerca')
    num_subway_map_col, num_subway_info_col = st.columns(2)
    subway_number = num_subway_info_col.number_input(
        'Cantidad de estaciones cerca',
        min_value=0,
        max_value=3)
    centers_by_subway_data = controller.get_center_by_subway_stop_number(subway_number)
    num_subway_info_col.dataframe(
        centers_by_subway_data.drop(['lat', 'lon'], axis=1),
        use_container_width=True)
    num_subway_map_col.map(centers_by_subway_data)

