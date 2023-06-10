import requests
import streamlit as st

TMDB_API_SECRET = st.secrets["TMDB_API_SECRET"]

def get_movie_posters(tmdb_id):
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}/images?include_image_language=en%2C%20null"
        headers = {
                "accept": "application/json",
                "Authorization": "Bearer " + TMDB_API_SECRET
                }

        response = requests.get(url, headers=headers)
        tmdb_json = response.json()
        file_path = tmdb_json['posters'][1]['file_path']
        url_poster = f"https://image.tmdb.org/t/p/w500/{file_path}"
        return url_poster  # Return the list of URL posters

