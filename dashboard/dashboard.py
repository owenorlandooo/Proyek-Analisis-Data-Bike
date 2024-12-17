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
df['holiday'] = df['holiday'].map({1: 'Holiday', 0: 'Not Holiday'})

# Sidebar filter untuk musim dan cuaca
season_filter = st.sidebar.multiselect("Pilih Musim", df['season'].unique(), default=df['season'].unique())
weather_filter = st.sidebar.multiselect("Pilih Kondisi Cuaca", df['weathersit'].unique(), default=df['weathersit'].unique())

# Filter data berdasarkan input pengguna
filtered_df = df[(df['season'].isin(season_filter)) & (df['weathersit'].isin(weather_filter))]

# Visualisasi Rata-rata Penyewaan Berdasarkan Musim
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=filtered_df, estimator='mean', palette='viridis')
plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
plt.xlabel("Musim")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi Rata-rata Penyewaan Berdasarkan Kondisi Cuaca
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weathersit', y='cnt', data=filtered_df, estimator='mean', palette='coolwarm')
plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi Rata-rata Penyewaan: Weekday vs Weekend
st.subheader("Rata-rata Penyewaan Sepeda: Weekday vs Weekend")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='workingday', y='cnt', data=filtered_df, estimator='mean', palette='muted')
plt.title("Rata-rata Penyewaan Sepeda: Weekday vs Weekend")
plt.xlabel("Tipe Hari")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi Rata-rata Penyewaan: Holiday vs Non-Holiday
st.subheader("Rata-rata Penyewaan Sepeda: Holiday vs Non-Holiday")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='holiday', y='cnt', data=filtered_df, estimator='mean', palette='Blues')
plt.title("Rata-rata Penyewaan Sepeda: Holiday vs Non-Holiday")
plt.xlabel("Tipe Hari")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)