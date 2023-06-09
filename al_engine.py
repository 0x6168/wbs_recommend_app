
import streamlit as st
import pandas as pd


url_links = './data/links.csv'
url_movies = './data/movies.csv'
url_ratings = './data/ratings.csv'
url_tags = './data/tags.csv'
url_pg16 = './data/pg16.csv'
url_kids = './data/kids.csv'
links_df = pd.read_csv(url_links)
movies_df = pd.read_csv(url_movies)
ratings_df = pd.read_csv(url_ratings)
tags_df = pd.read_csv(url_tags)
kids_df = pd.read_csv(url_kids)
pg16 = pd.read_csv(url_pg16)


# introduce the average rating and the rating count
popularity = pg16[['movieId', 'rating']].groupby(
    by='movieId').agg(avg_rating=("rating", "mean"))
popularity['rating_count'] = ratings_df[['movieId', 'rating']].groupby(
    by='movieId').agg(rating_count=("rating", "count"))['rating_count']

def recommend_popular_movies(n, df, weight_counts):
    # This function linearly combines ratings and counts with appropriate weights

    # Error message
    if weight_counts < 0 or weight_counts > 1:
        print("Weight must be in [0, 1]")

    # Scaling of the data
    from sklearn.preprocessing import MinMaxScaler
    my_scaler = MinMaxScaler().set_output(transform="pandas")
    my_scaler.fit(df)
    df1 = my_scaler.transform(df)

    col_name = f"lin. {weight_counts*100}%"
    df1[col_name] = weight_counts * df1['rating_count'] + \
        (1 - weight_counts) * df1['avg_rating']
    df1 = df1.merge(movies_df, how="left", on='movieId')[['title', 'genres']]
    
    return df1.head(n) #.sort_values(by=col_name, ascending=False).head(n)

# kids 

popularity_kids = kids_df[['movieId', 'rating']].groupby(
    by='movieId').agg(avg_rating=("rating", "mean"))
popularity_kids['rating_count'] = ratings_df[['movieId', 'rating']].groupby(
    by='movieId').agg(rating_count=("rating", "count"))['rating_count']

def recommend_popular_movies_kids(n, df, weight_counts):
    # This function linearly combines ratings and counts with appropriate weights

    # Error message
    if weight_counts < 0 or weight_counts > 1:
        print("Weight must be in [0, 1]")

    # Scaling of the data
    from sklearn.preprocessing import MinMaxScaler
    my_scaler = MinMaxScaler().set_output(transform="pandas")
    my_scaler.fit(df)
    df1 = my_scaler.transform(df)

    col_name = f"lin. {weight_counts*100}%"
    df1[col_name] = weight_counts * df1['rating_count'] + \
        (1 - weight_counts) * df1['avg_rating']
    df1 = df1.merge(movies_df, how="left", on='movieId')[['title', 'genres']]
    
    return df1.head(n) #.sort_values(by=col_name, ascending=False).head(n)