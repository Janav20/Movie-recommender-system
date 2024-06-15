import streamlit as st
import pickle
import requests

# Function to fetch poster from The Movie Database API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

# Function to fetch additional movie details
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    return {
        "genres": ", ".join([genre['name'] for genre in data['genres']]),
        "release_date": data.get('release_date', 'N/A'),
        "overview": data.get('overview', 'No overview available.')
    }

# Function to get recommendations
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_details = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_details.append(fetch_movie_details(movie_id))

    return recommended_movie_names, recommended_movie_posters, recommended_movie_details

# Title and Header
st.title("🎬 Movie Recommender System")
st.subheader("Find Your Next Favorite Movie!")
st.write("Explore movie recommendations based on your favorite titles. Simply select a movie and get top recommendations tailored just for you.")

# Load data
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Dropdown to select movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_details = recommend(selected_movie)
    for i in range(5):
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(recommended_movie_posters[i])
            with col2:
                st.markdown(f"**{recommended_movie_names[i]}**")
                st.markdown(f"**Genres:** {recommended_movie_details[i]['genres']}")
                st.markdown(f"**Release Date:** {recommended_movie_details[i]['release_date']}")
                st.markdown(f"**Overview:** {recommended_movie_details[i]['overview']}")
                st.write("")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        text-align: center;
        padding: 1rem;
        background: black;
        color: white;
    }
    </style>
    <div class="footer">
        Made with 💖 by Janav Shetty
    </div>
    """,
    unsafe_allow_html=True
)
