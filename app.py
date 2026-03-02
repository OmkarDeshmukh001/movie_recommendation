import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = movies['title']


# 🔹 Fetch poster from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4b1d4c2d4d0937cb0beab8906e429401&language=en-US"
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# 🔹 Recommendation function
def recommend(movie):
    movie_index = movies_list[movies_list == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# 🔹 UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie", movies_list)

if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    for col, name, poster in zip(
            [col1, col2, col3, col4, col5], names, posters):
        with col:
            st.text(name)
            st.image(poster)
