
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('dashboard/hour.csv')

# Title
st.title("Bike Sharing Data Analysis")

# Pilihan visualisasi
visual_choice = st.sidebar.selectbox("Pilih Visualisasi", ["Total Penggunaan Sepeda per Musim", "Penggunaan Sepeda per Jam dalam Sehari"])

# Visualisasi 1: Total Penggunaan Sepeda per Musim (Bar Chart)
if visual_choice == "Total Penggunaan Sepeda per Musim":
    st.header("Total Penggunaan Sepeda per Musim")

    # Menghitung total penggunaan sepeda per musim
    seasonal_usage = data.groupby('season')['cnt'].sum().reset_index()
    seasonal_usage['season'] = seasonal_usage['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

    # Membuat visualisasi (bar chart sesuai dengan yang di Colab)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(seasonal_usage['season'], seasonal_usage['cnt'], color=['lightgreen', 'lightblue', 'orange', 'lightcoral'])
    ax.set_title('Total Bike Usage by Season', fontsize=16)
    ax.set_xlabel('Season', fontsize=12)
    ax.set_ylabel('Total Usage', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Visualisasi 2: Penggunaan Sepeda per Jam dalam Sehari (Line Chart)
if visual_choice == "Penggunaan Sepeda per Jam dalam Sehari":
    st.header("Penggunaan Sepeda per Jam dalam Sehari")

    # Menghitung rata-rata penggunaan sepeda per jam
    hourly_usage = data.groupby('hr')['cnt'].mean().reset_index()

    # Membuat visualisasi (line chart sesuai dengan yang di Colab)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hourly_usage['hr'], hourly_usage['cnt'], marker='o', color='b')
    ax.set_title('Average Bike Usage by Hour of Day', fontsize=16)
    ax.set_xlabel('Hour of Day', fontsize=12)
    ax.set_ylabel('Average Bike Usage (cnt)', fontsize=12)
    ax.grid(True)
    st.pyplot(fig)
    
