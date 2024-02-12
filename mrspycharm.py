import pickle
import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

st.markdown(
    f"""
    <style>
    .stApp{{
        background-image: linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)),url("https://miro.medium.com/max/1200/1*oRJYoC18Msc4tC6FExYRKQ.jpeg");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=330eef6c814e0e1aa45a1d1e8e9b9a0f&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Check for new movies (for demonstration purposes)
def is_new_movie(release_date):
    current_date = datetime.now()
    movie_release_date = datetime.strptime(release_date, "%Y-%m-%d")
    days_since_release = (current_date - movie_release_date).days
    return days_since_release <= 7  # Consider movies released in the last 7 days as new

# Check if the 'release_date' column exists in the DataFrame
if 'release_date' in movies.columns:
    new_movies_available = any(is_new_movie(movie['release_date']) for _, movie in movies.iterrows())
else:
    new_movies_available = False

# Display notification bar for new movies
if new_movies_available:
    st.warning("**🚀New movies are now available! Check them out.**")
else:
    st.success("**✅No new movies at the moment. Stay tuned for updates.**")
# Display the rest of the Streamlit app
st.title('Movie Recommendation System')
st.markdown("<h2 style='text-align: left; color: #1f1f1f; font-weight: bold;'>Select your movie</h2>", unsafe_allow_html=True)
selected_movie_name = st.selectbox('', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"<h3 style='font-size: 18px;'>{names[0]}</h3>", unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(f"<h3 style='font-size: 18px;'>{names[1]}</h3>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f"<h3 style='font-size: 18px;'>{names[2]}</h3>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f"<h3 style='font-size: 18px;'>{names[3]}</h3>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f"<h3 style='font-size: 18px;'>{names[4]}</h3>", unsafe_allow_html=True)
        st.image(posters[4])