import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import pydeck as pdk

caminho_arquivo = '/Users/aniziocp/Desktop/PersonalProjects/toronto-real-state-scraping/toronto_data-acum-v1.csv'
dataframe = pd.read_csv(caminho_arquivo)

dataframe = pd.read_csv(caminho_arquivo)
dataframe = dataframe[dataframe['Price']!='$X,XXX'] #retirando linhas com o valor 'X,XXX'.
dataframe = dataframe[dataframe['Price']!='$XXX,XXX']
dataframe = dataframe[dataframe['Bedrooms']!='Ausente']
dataframe = dataframe[dataframe['Walk Score']!='–']
dataframe = dataframe[dataframe['Status']=='Lease']
dataframe['Price'] = dataframe['Price'].apply(lambda x : float(x[1:].replace(',', ''))) #retirando o $ na frente dos preços.
dataframe['Walk Score'] = dataframe['Walk Score'].apply(lambda x : float(x))
dataframe['Bedrooms'] = dataframe['Bedrooms'].apply(lambda x : float(x)) 
dataframe['Bathrooms'] = dataframe['Bathrooms'].apply(lambda x : float(x))
dataframe['Kitchens'] = dataframe['Kitchens'].apply(lambda x : float(x))
dataframe['Rooms'] = dataframe['Rooms'].apply(lambda x : float(x))
dataframe['Bedroom Plus'] = dataframe['Bedroom Plus'].apply(lambda x : float(x))
dataframe['Room Plus'] = dataframe['Room Plus'].apply(lambda x : float(x))
dataframe['Size'] = dataframe['Size'].apply(lambda x : x.replace('sqft', ''))
dataframe['Size_min'] = dataframe['Size'].apply(lambda x : float(x.split("-")[0].strip()))
dataframe['Size_max'] = dataframe['Size'].apply(lambda x : float(x.split("-")[1].strip()))
dataframe['Size_mean'] = (dataframe['Size_min'] + dataframe['Size_max'])/2
dataframe = dataframe.drop(columns=['Status', 'Area', 'Age_cabecalho', 'Size'])

st.title("Toronto properties prices for lease")

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Data Analysis", "Prediction"])

with tab1:
    # load a sample dataset as a pandas DataFrame
    alt.data_transformers.disable_max_rows()
    # make the chart
    alt_chart = alt.Chart(dataframe).mark_point().encode(
        x='Size_mean',y='Price',color='Private Entrance').interactive().properties(
        width=800,  # Adjust the width as needed
        height=400  # Adjust the height as needed
    )
    st.write(alt_chart)

    # Sample data: latitude and longitude of some locations


    # Latitude and longitude for Toronto's city center
    TORONTO_LATITUDE = 43.651070
    TORONTO_LONGITUDE = -79.347015

    # Define the initial view state for the PyDeck map
    view_state = pdk.ViewState(
        latitude=TORONTO_LATITUDE,
        longitude=TORONTO_LONGITUDE,
        zoom=10,  # Zoom level 10 to have a city-wide view
        pitch=0
    )

    # Define a PyDeck layer to display (optional)
    # This example does not add any layer but focuses on Toronto
    layer = []

    # Create the PyDeck map
    toronto_map = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state,layers=[layer],)

    # Display the map in Streamlit
    st.pydeck_chart(toronto_map)
    

#st.button('Hit me')
#st.data_editor('Edit data', data)
#st.checkbox('Check me out')
#st.radio('Pick one:', ['nose','ear'])
#st.selectbox('Select', [1,2,3])
#st.multiselect('Multiselect', [1,2,3])
#st.slider('Slide me', min_value=0, max_value=10)
###st.select_slider('Slide to select', options=[1,'2'])
#st.text_input('Enter some text')
#st.number_input('Enter a number')
#st.text_area('Area for textual entry')
#st.date_input('Date input')
#st.time_input('Time entry')
#st.file_uploader('File uploader')
#st.download_button('On the dl', data)
#st.camera_input("一二三,茄子!")
#st.color_picker('Pick a color')
