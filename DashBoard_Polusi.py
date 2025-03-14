import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import folium
from streamlit_folium import folium_static 
from scipy.stats.mstats import winsorize
from sklearn.cluster import KMeans
import numpy as np

# Load dataset
file_path = "dataset_hasil.csv"
df = pd.read_csv(file_path)

# Membersihkan data (Clearing data)
polusi_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
df[polusi_cols] = df[polusi_cols].fillna(df[polusi_cols].median())

cuaca_cols = ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
df[cuaca_cols] = df[cuaca_cols].fillna(df[cuaca_cols].mean())

df["wd"] = df["wd"].fillna(df["wd"].mode()[0])

# Winsorizing untuk outlier
df[polusi_cols] = df[polusi_cols].apply(lambda x: winsorize(x, limits=[0.01, 0.01]))
df[cuaca_cols] = df[cuaca_cols].apply(lambda x: winsorize(x, limits=[0.01, 0.01]))

# Konversi datetime jika masih dalam format string
df["datetime"] = pd.to_datetime(df["datetime"], errors='coerce')

# Cek apakah konversi berhasil
print(df["datetime"].dtype)  # Harusnya output 'datetime64[ns]'

# Rata-rata polusi harian
df["date"] = df["datetime"].dt.date
daily_avg = df.groupby("date")[polusi_cols].mean().reset_index()

# Polusi per Musim
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["datetime"].dt.month.apply(get_season)

#Dashboard
st.set_page_config(page_title="Dashboard Polusi Udara", layout="wide")
st.markdown("""
<style>
    * {
        font-family: 'Times New Roman', serif !important;
    }
    .main {
        background-color: #f5f5f5;
    }
    .stSidebar {
        background-color: #2c3e50;
        color: white;
    }
    .stTitle, .stHeader, .stSubheader {
        color: #2c3e50;
    }
    label, .stSelectbox div, .stTextInput div, .stNumberInput div {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title('Dashboard Analisis Polusi Udara dan Cuaca')

# Sidebar
with st.sidebar:
    st.header("Pengaturan Dashboard")
    selected_year = st.selectbox("Pilih Periode Tahun", df["datetime"].dt.year.unique(), format_func=lambda x: f"{x}")
    selected_month = st.selectbox("Pilih Periode Bulan", df["datetime"].dt.month.unique(), format_func=lambda x: f"Bulan {x}")
    pollutant = st.selectbox('Pilih untuk Visualisasi', polusi_cols)

# Filter data berdasarkan tahun dan bulan
filtered_df = df[(df["datetime"].dt.year == selected_year) & (df["datetime"].dt.month == selected_month)]

# Layout menggunakan columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Tren {pollutant} Seiring Waktu")
    st.markdown("Visualisasi ini menunjukkan tren konsentrasi polusi dalam satu bulan yang dipilih.")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=filtered_df, x="datetime", y=pollutant, ax=ax, label=pollutant, color="red", alpha=0.7)
    plt.xlabel("Tahun")
    plt.ylabel(f"Konsentrasi {pollutant}")
    plt.title(f"Tren {pollutant} Seiring Waktu")
    plt.legend()
    st.pyplot(fig)

st.subheader("Heatmap Korelasi")
st.markdown("Heatmap ini menunjukkan hubungan antara berbagai polusi dan variabel cuaca.")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[polusi_cols + cuaca_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", center=0)
st.pyplot(fig)

# Peta interaktif
st.subheader("Peta Distribusi Polusi Udara")
st.markdown("Peta ini menunjukkan distribusi polusi udara berdasarkan data sampel.")
m = folium.Map(location=[39.9, 116.4], zoom_start=10)
for i, row in df.sample(100).iterrows():
    folium.CircleMarker(
        location=[39.9 + np.random.uniform(-0.05, 0.05), 116.4 + np.random.uniform(-0.05, 0.05)],
        radius=row["PM2.5"] / 10,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(m)
folium_static(m)

st.subheader("Data Setelah Pembersihan")
st.dataframe(df.head())
