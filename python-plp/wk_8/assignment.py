# 📊 CORD-19 Metadata Explorer
# Combined script for data loading, cleaning, analysis, and Streamlit app

# -------------------------------
# Part 1: Data Loading & Exploration
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("metadata.csv")

print("Shape:", df.shape)
print(df.info())
print(df.isnull().sum().sort_values(ascending=False).head(10))
print(df.describe())

# -------------------------------
# Part 2: Data Cleaning & Preparation
# -------------------------------
# Drop rows missing essential info
df_clean = df.dropna(subset=["title", "publish_time"])

# Convert dates
df_clean["publish_time"] = pd.to_datetime(df_clean["publish_time"], errors="coerce")
df_clean["year"] = df_clean["publish_time"].dt.year

# Abstract word count
df_clean["abstract_word_count"] = df_clean["abstract"].fillna("").apply(lambda x: len(x.split()))

print(df_clean.head())

# -------------------------------
# Part 3: Data Analysis & Visualization
# -------------------------------
# Publications by year
year_counts = df_clean["year"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Top journals
top_journals = df_clean["journal"].value_counts().head(10)
top_journals.plot(kind="barh", figsize=(8, 5), title="Top Journals")
plt.show()

# Word Cloud from titles
all_titles = " ".join(df_clean["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_titles)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Titles")
plt.show()

# -------------------------------
# Part 4: Streamlit Application
# -------------------------------
import streamlit as st

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (metadata.csv)")

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()

# Interactive filter
year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select year range", year_min, year_max, (2020, 2021))
df_filtered = df[df["year"].between(year_range[0], year_range[1])]

st.write("Dataset preview", df_filtered.head())

# Publications by year
st.subheader("Publications by Year")
year_counts = df_filtered["year"].value_counts().sort_index()
st.bar_chart(year_counts)

# Top journals
st.subheader("Top Journals")
st.bar_chart(df_filtered["journal"].value_counts().head(10))

# Word Cloud
st.subheader("Word Cloud of Titles")
titles = " ".join(df_filtered["title"].dropna().tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(titles)
st.image(wc.to_array())
