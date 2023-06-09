
import streamlit as st
import pandas as pd
import surprise
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import train_test_split
from surprise import Reader
from surprise import KNNBasic, SVD
from surprise import accuracy


url_pg16 = './data/pg16.csv'
pg16 = pd.read_csv(url_pg16)
reader = Reader(rating_scale=(0.5, 5))  # Set the rating scale according to data
data = Dataset.load_from_df(pg16[["userId", "movieId", "rating"]], reader)
# Split the data into train and test sets
trainset, testset = train_test_split(data, test_size=0.25)

def recommend_movies_GRID(user_id):
    # # Set the best parameters
    # best_n_factors = 150
    # best_n_epochs = 30
    # best_lr_all = 0.01
    # best_reg_all = 0.05

    # Create the SVD model with the best parameters
    algo = SVD(n_factors=150, n_epochs=30, lr_all=0.01, reg_all=0.05)

    # Fit the model to the trainset
    algo.fit(trainset)

    # Get a list of all the movies the user has not rated
    all_movies = pg16['movieId'].unique()
    user_movies = pg16[pg16['userId'] == user_id]['movieId'].unique()
    new_movies = list(set(all_movies) - set(user_movies))

    # Predict the ratings for the new movies
    predictions = [algo.predict(user_id, movie_id) for movie_id in new_movies]

    # Sort the predictions by estimated rating
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get the top 10 recommendations with title names
    top_recommendations = [(prediction.iid, pg16[pg16['movieId'] == prediction.iid]['title'].values[0]) for prediction in predictions[:10]]
    top_recommendations = pd.DataFrame(top_recommendations)
    top_recommendations = top_recommendations.rename(columns={1: 'suggested movies'})
    top_recommendations = top_recommendations['suggested movies']
    top_recommendations.reset_index(drop=True, inplace=True)
    # Add 1 to the index values
    top_recommendations.index = top_recommendations.index + 1
    return top_recommendations


def recommend_movies_GENRES(user_id, genre, decade):
    # Set the best parameters
    best_n_factors = 150
    best_n_epochs = 30
    best_lr_all = 0.01
    best_reg_all = 0.05

    # Create the SVD model with the best parameters
    algo = SVD(n_factors=best_n_factors, n_epochs=best_n_epochs, lr_all=best_lr_all, reg_all=best_reg_all)

    # Fit the model to the trainset
    algo.fit(trainset)

    # Get a list of all the movies the user has not rated
    all_movies = pg16['movieId'].unique()
    user_movies = pg16[pg16['userId'] == user_id]['movieId'].unique()
    new_movies = list(set(all_movies) - set(user_movies))

    # Filter new movies by genre
    genre_movies = pg16[pg16['genres'].str.contains(genre, case=False)]
    decade_movies = pg16[pg16['decade'].isin([decade])]
    new_movies_genre = list(set(genre_movies['movieId']) & set(new_movies) & set(decade_movies['movieId']))

    # Predict the ratings for the new movies in the specified genre
    predictions = [algo.predict(user_id, movie_id) for movie_id in new_movies_genre]

    # Sort the predictions by estimated rating
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get the top 10 recommendations with title names
    top_recommendations = [(prediction.iid, pg16[pg16['movieId'] == prediction.iid]['title'].values[0]) for prediction in predictions[:10]]
    top_recommendations = pd.DataFrame(top_recommendations)
    top_recommendations = top_recommendations.rename(columns={1: 'suggested movies'})
    top_recommendations = top_recommendations['suggested movies']
    top_recommendations.reset_index(drop=True, inplace=True)
    # Add 1 to the index values
    top_recommendations.index = top_recommendations.index + 1
    return top_recommendations
