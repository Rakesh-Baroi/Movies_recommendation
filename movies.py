import streamlit as st
import pandas as pd

try:
    df = pd.read_csv("movies_data.csv")
except FileNotFoundError:
    st.error("Error: 'movies_data.csv' not found. Please make sure the dataset is in the same directory as the app file.")
    st.stop() 


st.title("Movie Recommendation System")
st.write("Get movie recommendations based on your preferred language and genre.")

# Get user preferences for movie type using Streamlit widgets
languages = ['Hollywood', 'Bollywood', 'Regional'] 
genres = sorted(df['primary_genre'].unique().tolist()) 

preferred_language = st.selectbox("Select your preferred language:", languages)
preferred_genre = st.selectbox("Select your preferred genre:", genres)

if st.button("Get Recommendations"):
    st.write(f"\nLooking for movies in {preferred_language} language with genre {preferred_genre}...")

    # Filter the dataset based on user preferences
    recommended_movies = df[
        (df['language_type'] == preferred_language) &
        (df['primary_genre'] == preferred_genre)
    ]

    recommended_movies = recommended_movies.sort_values(by=['vote_average', 'popularity'], ascending=False)

    if not recommended_movies.empty:
        st.subheader("Top Recommended Movies matching your preferences:")
        for i, row in recommended_movies.head(5).iterrows():
            st.write(f"- **{row['Title']}** (Rating: {row['vote_average']}, Popularity: {row['popularity']})")
    else:
        st.write("\nSorry, no movies found matching your preferred language and genre.")

st.markdown("""
---
**ThanQ for visiting our web sit**
Great movies are weating for you.
let me know if you want to add somthing        
""")
