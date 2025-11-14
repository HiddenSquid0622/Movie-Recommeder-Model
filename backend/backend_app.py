from fastapi import FastAPI
from pydantic import BaseModel
from models.recommender import load_recommender, recommend_movies

app = FastAPI()
df, combined_features = load_recommender()


@app.get("/")
def root():
    return {"message": "Welcome to the Movie Recommender System !"}


class MovieInput(BaseModel):
    movie_name: str
    n: int


@app.post("/recommend")
def recommend(data: MovieInput):
    recommendations = recommend_movies(data.movie_name, df, combined_features, data.n)

    if not recommendations:
        return {"error": f"Movie '{data.movie_name}' not found in the dataset."}

    return {"recommended_movies": recommendations}
