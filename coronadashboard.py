import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("🦠 COVID-19 Data Analysis Dashboard")

# -----------------------------------
# LOAD DATA
# -----------------------------------
df = pd.read_csv("D:\\CODES24\\project2\\2019_nCoV_20200121_20200206.csv")



# -----------------------------------
# DATA CLEANING
# -----------------------------------
df['Province/State'].fillna('Unknown', inplace=True)
df['Confirmed'].fillna(df['Confirmed'].median(), inplace=True)
df['Death'].fillna(df['Death'].median(), inplace=True)
df['Recovered'].fillna(df['Recovered'].median(), inplace=True)
df['Suspected'].fillna(0, inplace=True)

df["Last Update"] = pd.to_datetime(df["Last Update"], errors="coerce")

# -----------------------------------
# SIDEBAR FILTER
# -----------------------------------
st.sidebar.header("🔍 Filters")

country = st.sidebar.selectbox(
    "Select Country",
    sorted(df['Country/Region'].unique())
)

country_df = df[df['Country/Region'] == country]

# -----------------------------------
# KPI METRICS
# -----------------------------------
total_confirmed = int(country_df['Confirmed'].sum())
total_recovered = int(country_df['Recovered'].sum())
total_death = int(country_df['Death'].sum())

c1, c2, c3 = st.columns(3)
c1.metric("😷 Confirmed", f"{total_confirmed:,}")
c2.metric("💚 Recovered", f"{total_recovered:,}")
c3.metric("⚰ Deaths", f"{total_death:,}")

# -----------------------------------
# BAR CHART (Province Wise)
# -----------------------------------
st.subheader("📊 Province-wise Cases")

province_data = country_df.groupby('Province/State')[['Confirmed','Recovered','Death']].sum()

fig1, ax1 = plt.subplots(figsize=(10,5))
province_data.plot(kind='bar', ax=ax1)
ax1.set_xlabel("Province / State")
ax1.set_ylabel("Cases")
ax1.set_title(f"COVID-19 Cases in {country}")
ax1.grid(True)

st.pyplot(fig1)

# -----------------------------------
# TIME SERIES TREND
# -----------------------------------
st.subheader("📈 COVID-19 Trend Over Time")

time_series = country_df.groupby(
    country_df["Last Update"].dt.date
)[['Confirmed','Recovered','Death']].sum()

fig2, ax2 = plt.subplots(figsize=(10,5))
ax2.plot(time_series.index, time_series['Confirmed'], label="Confirmed")
ax2.plot(time_series.index, time_series['Recovered'], label="Recovered")
ax2.plot(time_series.index, time_series['Death'], label="Death")
ax2.set_xlabel("Date")
ax2.set_ylabel("Cases")
ax2.set_title("COVID-19 Growth Trend")
ax2.legend()
ax2.grid(True)

st.pyplot(fig2)

# -----------------------------------
# PIE CHART
# -----------------------------------
st.subheader("🥧 Case Distribution")

values = [
    total_confirmed,
    total_recovered,
    total_death
]
labels = ["Confirmed", "Recovered", "Death"]

fig3, ax3 = plt.subplots(figsize=(6,6))
ax3.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    explode=(0.05,0.05,0.05)
)
ax3.set_title("COVID-19 Case Distribution")

st.pyplot(fig3)

# -----------------------------------
# DATA TABLE
# -----------------------------------
st.subheader("📋 Raw Data")
st.dataframe(country_df)
