import streamlit as st
import pickle
import ast
import requests
import os
import gdown

if not os.path.exists("similarity.pkl") or os.path.getsize("similarity.pkl") < 1000000:
    with st.spinner("Downloading similarity file, please wait..."):
        gdown.download("https://drive.google.com/uc?id=1OBs-6uB-wyW-rHogZQDIVViEDVGHpCwb", "similarity.pkl", quiet=False, fuzzy=True)

movies  = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
             

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY"
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:6]

    names = []
    posters = []

    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return names, posters


st.title('Movie Recommender System')
selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
import streamlit as st
import pickle
import ast
import requests

movies  = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
                              

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY"
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:6]

    names = []
    posters = []

    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return names, posters


st.title('Movie Recommender System')
selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
