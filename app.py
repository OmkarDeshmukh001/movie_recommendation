import streamlit as st
import pickle
import requests
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# Load Movies
# ==============================


@st.cache_data
def load_movies():
    return pickle.load(open("movies.pkl", "rb"))


movies = load_movies()
movies_list = movies["title"]


# ==============================
# Load or Generate Similarity
# ==============================
@st.cache_data
def load_similarity():
    if os.path.exists("similarity.pkl"):
        return pickle.load(open("similarity.pkl", "rb"))

    # 🔥 Generate if missing (Render safe)
    similarity_matrix = cosine_similarity(movies["tags"].tolist())

    # Save locally (optional)
    try:
        with open("similarity.pkl", "wb") as f:
            pickle.dump(similarity_matrix, f)
    except:
        pass

    return similarity_matrix


similarity = load_similarity()


# ==============================
# Fetch poster from TMDB
# ==============================
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4b1d4c2d4d0937cb0beab8906e429401&language=en-US"
        data = requests.get(url, timeout=10).json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"


# ==============================
# Recommendation function
# ==============================
def recommend(movie):
    movie_index = movies_list[movies_list == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]["movie_id"]
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ==============================
# UI
# ==============================
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie", movies_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)
