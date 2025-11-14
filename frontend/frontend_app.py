import streamlit as st
import requests

st.title("Movie Recommendation System")
st.write("Enter a movie name and how many recommendations you want:")

movie_name = st.text_input(
    "Movie name", placeholder="Enter a movie name (e.g. Inception)"
)
num_recommend = st.number_input(
    "Number of recommendations", min_value=1, max_value=20, value=5, step=1
)

if st.button("Get Recommendations"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        payload = {"movie_name": movie_name, "n": int(num_recommend)}
        try:
            res = requests.post(
                "https://movie-recommeder-model.onrender.com/recommend", json=payload
            )
            if res.status_code == 200:
                data = res.json()
                recs = data.get("recommended_movies", [])
                if recs:
                    st.success(f"Top {len(recs)} movies similar to '{movie_name}':")
                    for i, r in enumerate(recs, 1):
                        st.write(f"{i}. {r}")
                else:
                    st.error("No recommendations found. Try another movie.")
            else:
                st.error(f"Error {res.status_code}: {res.text}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")
