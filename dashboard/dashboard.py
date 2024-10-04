import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('dashboard/hour.csv')

# Title
st.title("Bike Sharing Data Analysis")

# Pilihan visualisasi
visual_choice = st.sidebar.selectbox("Pilih Visualisasi", ["Pengaruh Suhu terhadap Penyewaan", "Jumlah Penyewaan per Jam"])

# Visualisasi 1: Pengaruh Suhu terhadap Jumlah Penyewaan
if visual_choice == "Pengaruh Suhu terhadap Penyewaan":
    st.header("Pengaruh Suhu terhadap Jumlah Penyewaan")
    fig, ax = plt.subplots()
    sns.scatterplot(x='temp', y='cnt', data=data, ax=ax)
    st.pyplot(fig)

# Visualisasi 2: Jumlah Penyewaan per Jam
if visual_choice == "Jumlah Penyewaan per Jam":
    st.header("Jumlah Penyewaan per Jam")
    fig, ax = plt.subplots()
    sns.barplot(x='hr', y='cnt', data=data, ax=ax)
    st.pyplot(fig)
    
