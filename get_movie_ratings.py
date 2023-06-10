import pandas as pd

url_links = './data/links.csv'
url_movies = './data/movies.csv'
url_ratings = './data/ratings.csv'
url_tags = './data/tags.csv'

links_df = pd.read_csv(url_links)
movies_df = pd.read_csv(url_movies)
ratings_df = pd.read_csv(url_ratings)
tags_df = pd.read_csv(url_tags)


# merge movies, ratings, links dfs
movies_ratings_links = ratings_df.merge(movies_df, how="left", on="movieId").merge(links_df, how='left', on="movieId")
# get mean rating for each tmdb_id
mean_rating_df = movies_ratings_links.groupby(['tmdbId', 'title']).agg({'rating':'mean'}).reset_index()

def get_movie_rating(tmdb_id):
    rating = mean_rating_df.loc[mean_rating_df['tmdbId']==tmdb_id]['rating'].round(1).item()  
    return rating
