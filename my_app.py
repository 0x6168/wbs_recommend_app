import pandas as pd
import numpy as np
import streamlit as st
from al_engine import recommend_popular_movies
from al_engine import recommend_popular_movies_kids
from al_engine import popularity
from al_engine import popularity_kids
from szani_engine import recommend_movies_GENRES
from szani_engine import recommend_movies_GRID
import surprise
# from PIL import Image

# image = Image.open('dvd_store.jpg')
#st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")



with st.sidebar:
        st.image('images/dvd_store.jpg',use_column_width='always')
        st.write('The current most & best rated movie is ')
        st.write('_Forest Gump_')
        st.write('Rate what you saw to see your favorite movie displayed here!')
st.title(":blue[Ursula's secret movie algorithm]")



col1, col2 = st.columns(2)

with col1:
    st.subheader("All-time favorites for adults:")
    st.write(recommend_popular_movies(5, popularity, 0.8))
with col2: 
    st.subheader("For all you kids out there:")
    st.write(recommend_popular_movies(5, popularity_kids, 0.7))

# -----------------------------------------------------------------------------------------------------------

st.divider()
st.header(":blue[Talk to Ursula!]")
col7, col8 = st.columns([0.7, 0.3])
with col7:
    st.subheader("Who are you? Your UserId is enough ;-)")
with col8:
    user_id = st.number_input(label="Input your UserId", min_value=1,value=1, disabled=False, label_visibility="visible")
st.divider()
st.subheader(f'Hello {user_id}, I have the following suggestions for you:')
col9, col10 = st.columns([0.7, 0.3])
with col9:
    st.write(recommend_movies_GRID(user_id))
with col10:
    st.image('images/dvd_pile.jpg',use_column_width='always')
st.divider()
st.subheader("Feeling nostalgic? Want a certain genre?")
col3, col4 = st.columns(2)
with col3:
    genre = st.selectbox(
    'Select your favorite genre',
    ('Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'))
with col4:
    decade = st.selectbox(
    'Where do you want to timetravel to?',
    (1920, 1930, 1940,1950, 1960, 1970, 1980, 1990, 2000, 2010),index=9)
col5, col6 = st.columns(2)
with col5:
    st.subheader("These could be your tickets:")
    st.write(recommend_movies_GENRES(user_id, genre, decade))
with col6: 
    st.subheader("                           ")
    st.subheader("                           ")
    st.image('images/dvd_shelf.jpg',use_column_width='always')

