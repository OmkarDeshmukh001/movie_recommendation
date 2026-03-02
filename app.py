import streamlit as st
import pickle
import requests
import os
import numpy as np

st.set_page_config(page_title="Movie Recommender", layout="wide")

# ==============================
# Load Movies
# ==============================


@st.cache_data
def load_movies():
    with open("movies.pkl", "rb") as f:
        return pickle.load(f)


movies = load_movies()
movies_list = movies["title"].values


# ==============================
# Load Similarity (Drive Download)
# ==============================
@st.cache_data
def load_similarity():
    import gdown

    file_id = "1TwWbz3EKwDK-JVOcBzTJyG13Ro_tiAYd"
    url = f"https://drive.google.com/uc?id={file_id}"

    if not os.path.exists("similarity.npy"):
        with st.spinner("Downloading similarity matrix..."):
            gdown.download(url, "similarity.npy", quiet=False)

    return np.load("similarity.npy")


similarity = load_similarity()


# ==============================
# Fetch Poster
# ==============================
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4b1d4c2d4d0937cb0beab8906e429401&language=en-US"
        data = requests.get(url, timeout=10).json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        pass

    return "https://via.placeholder.com/500x750?text=No+Image"


# ==============================
# Recommend
# ==============================
def recommend(movie):
    idx = movies[movies["title"] == movie].index[0]
    distances = similarity[idx]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    names, posters = [], []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]["movie_id"]
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters


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
