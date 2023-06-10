import pandas as pd
import numpy as np
import streamlit as st
from al_engine import recommend_popular_movies
from al_engine import recommend_popular_movies_kids
from get_movie_posters import get_movie_posters
from al_engine import popularity
from al_engine import popularity_kids
from szani_engine import recommend_movies_GENRES
from szani_engine import recommend_movies_GRID
import surprise
from streamlit_star_rating import st_star_rating
from get_movie_ratings import get_movie_rating



with st.sidebar:
        st.image('images/dvd_store.jpg',use_column_width='always')
        st.write('The current most & best rated movie is ')
        st.write('_Forest Gump_')
        st.write('Want to see your favorite movie displayed here?')
        st.write('Start RATING!')
        st.divider()
        st. write("CREDITS")
        st.write("This product uses the TMDB API but is not endorsed or certified by TMDB.")
st.title(":blue[Ursula's secret movie algorithm]")




st.subheader("All-time favorites for adults:")
    
# st.image(recommend_popular_movies(5, popularity, 0.8)[0],use_column_width='always')
tmdb_id_list = recommend_popular_movies(5, popularity, 0.8)
col11, col12, col13, col14, col15 = st.columns(5)
col_list = [col11, col12, col13, col14, col15]
counter = 0

for tmdb_id in tmdb_id_list: 
        with col_list[counter]:
            st.image(get_movie_posters(tmdb_id), width=120)
            movie_rating = get_movie_rating(tmdb_id)
            st_star_rating(label = None, maxValue = 5, defaultValue = movie_rating, key = tmdb_id, read_only = True, size=16)

        counter += 1
    # st.write(tmbd_id)
st.divider()

st.subheader("For all you kids out there:")
tmdb_id_list_kids = recommend_popular_movies_kids(5, popularity_kids, 0.8)
kids1, kids2, kid3, kids4, kids5 = st.columns(5)
col_list = [kids1, kids2, kid3, kids4, kids5]
counter = 0

for tmdb_id in tmdb_id_list_kids: 
        with col_list[counter]:
            st.image(get_movie_posters(tmdb_id), width=120)
            movie_rating = get_movie_rating(tmdb_id)
            st_star_rating(label = None, maxValue = 5, defaultValue = movie_rating, key = tmdb_id, read_only = True, size=16)


        counter += 1

# -----------------------------------------------------------------------------------------------------------

st.divider()
st.header(":blue[Talk to Ursula!]")
col7, col8 = st.columns([0.7, 0.3])
with col7:
    st.subheader("Who are you? Your UserId is enough ;-)")
with col8:
    user_id = st.number_input(label="Input you UserId", min_value=1,value=1, disabled=False, label_visibility="visible")
st.divider()
st.subheader(f'Hello {user_id}, I have the following suggestions for you:')
st.write(recommend_movies_GRID(user_id))
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
    # st.subheader("These could be your tickets:")
    st.write(recommend_movies_GENRES(user_id, genre, decade))
with col6: 
    st.image('images/dvd_shelf.jpg',use_column_width='always')



