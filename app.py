import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV
df = pd.read_csv("SpotifyFeatures.csv")

# Dashboard title
st.title("Spotify Songs Dashboard")

#  Popularity Distribution
fig1 = px.histogram(df, x='popularity', nbins=30, title='Track Popularity Distribution')
st.plotly_chart(fig1)

#  Top 10 Artists by Number of Tracks
top_artists = df['artist_name'].value_counts().head(10)
fig2 = px.bar(x=top_artists.values, y=top_artists.index, orientation='h', title='Top 10 Artists by Number of Tracks')
st.plotly_chart(fig2)

# Danceability vs Popularity
fig3 = px.scatter(df, x='danceability', y='popularity', title='Danceability vs Popularity')
st.plotly_chart(fig3)

# Energy vs Popularity
fig4 = px.scatter(df, x='energy', y='popularity', 
                  title='Energy vs Popularity')
st.plotly_chart(fig4)

