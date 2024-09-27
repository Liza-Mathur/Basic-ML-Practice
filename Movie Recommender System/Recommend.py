import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
# from sklearn.metrics.pairwise import cosine_similarity
import requests

# def fetch_poster(movie_id):
#     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=6714f90fad9f040c44d6f6db0846306c".format(movie_id))
#     data = response.json()
#     return "http://image.tmdb.org/t/p/w500/" + data['poster_path'] # for id = 12 -- poster_path = /eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg

def fetch_poster(movie_id):
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=6714f90fad9f040c44d6f6db0846306c".format(movie_id))
        data = response.json()

        # Check if the response contains a valid 'poster_path'
        return f"http://image.tmdb.org/t/p/w500{data['poster_path']}"
        
    except Exception as e:
        print(f"An error occurred while fetching poster for movie ID {movie_id}: {e}")
        # Return default image in case of an error
        return f"http://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg"


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True, key = lambda x : x[1])[1:6]
    recommend = []
    posters=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        posters.append(fetch_poster(movie_id))
        recommend.append(movies.iloc[i[0]].title)
    return (recommend,posters)

movies_dict = pkl.load(open("new_df.pkl","rb"))
similarity = pkl.load(open("similarity.pkl","rb"))
movies = pd.DataFrame(movies_dict)
print(movies_dict.keys())
st.title("Movie Recommender System")

option = st.selectbox('Give us your favorite movie',movies['title'].values)
if st.button("Recommend"):
    recommendations, poster= recommend(option)
    # for i in recommendations:
    #     st.write(i)
    col1, col2, col3 , col4 , col5= st.columns(5)

    with col1:
        st.text(recommendations[0])
        st.image(poster[0])

    with col2:
        st.text(recommendations[1])
        st.image(poster[1])

    with col3:
        st.text(recommendations[2])
        st.image(poster[2])

    with col4:
        st.text(recommendations[3])
        st.image(poster[3])

    with col5:
        st.text(recommendations[4])
        st.image(poster[4])