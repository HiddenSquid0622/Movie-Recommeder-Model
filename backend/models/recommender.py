import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def load_recommender():
    df = pd.read_pickle("data/processed/df_clean.pkl")
    combined_features = np.load("data/processed/combined_features.npy")
    return df, combined_features


def recommend_movies(movie_name, df, combined_features, top_n=10):
    if movie_name not in df["original_title"].values:
        return []

    movie_id = df[df["original_title"] == movie_name]["id"].values[0]
    movie_idx = df[df["id"] == movie_id].index[0]

    similarities = cosine_similarity(
        combined_features[movie_idx].reshape(1, -1), combined_features
    ).flatten()

    similar_indices = similarities.argsort()[-top_n - 1 : -1][::-1]
    return df.iloc[similar_indices]["original_title"].tolist()
