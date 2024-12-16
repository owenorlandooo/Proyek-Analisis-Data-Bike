import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

base_path = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_path, "data", "day.csv")
df = pd.read_csv(data_path)

st.title("Bike Sharing Dashboard 🚲")
st.sidebar.header("Filter Data")

df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['weathersit'] = df['weathersit'].map({
    1: 'Clear', 
    2: 'Mist', 
    3: 'Light Rain/Snow', 
    4: 'Heavy Rain/Snow'
})
df['workingday'] = df['workingday'].map({1: 'Weekday', 0: 'Weekend'})
season_filter = st.sidebar.multiselect("Pilih Musim", df['season'].unique(), default=df['season'].unique())
filtered_df = df[df['season'].isin(season_filter)]
st.subheader("Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=filtered_df, estimator=sum, palette='viridis')
st.pyplot(fig)
st.subheader("Penggunaan Sepeda: Weekday vs Weekend")
fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=filtered_df, estimator=sum, palette='muted')
st.pyplot(fig)