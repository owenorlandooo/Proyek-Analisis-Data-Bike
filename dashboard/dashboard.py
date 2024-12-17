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

season_filter = st.sidebar.multiselect("Pilih Musim", df['season'].unique(), default=df['season'].unique())
weather_filter = st.sidebar.multiselect("Pilih Kondisi Cuaca", df['weathersit'].unique(), default=df['weathersit'].unique())
filtered_df = df[(df['season'].isin(season_filter)) & (df['weathersit'].isin(weather_filter))]

st.subheader("Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=filtered_df, estimator='mean', palette='viridis')
plt.xlabel("Musim")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

st.subheader("Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=filtered_df, estimator='mean', palette='coolwarm')
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

st.subheader("Tren Penyewaan Sepeda Berdasarkan Bulan")
df['month'] = pd.to_datetime(df['dteday']).dt.month
monthly_usage = filtered_df.groupby('month')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(x='month', y='cnt', data=monthly_usage, marker="o", color="blue")
plt.xlabel("Bulan")
plt.ylabel("Total Penyewaan Sepeda")
plt.title("Total Penyewaan Sepeda per Bulan")
st.pyplot(fig)

st.subheader("Penggunaan Sepeda: Weekday vs Weekend")
fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=filtered_df, estimator='mean', palette='muted')
plt.xlabel("Tipe Hari")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

st.subheader("Distribusi Kelompok Penyewaan Sepeda")
df['usage_group'] = pd.qcut(df['cnt'], q=3, labels=['Rendah', 'Sedang', 'Tinggi'])
fig, ax = plt.subplots()
sns.countplot(x='usage_group', data=filtered_df, palette='coolwarm')
plt.xlabel("Kategori Penyewaan")
plt.ylabel("Jumlah Hari")
plt.title("Distribusi Kelompok Penyewaan Sepeda")
st.pyplot(fig)