import streamlit as st
import pandas as pd
from embedding import get_embedding
from endee_db import EndeeDB

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")


# Load & Cache Database

@st.cache_resource
def load_db():
    df = pd.read_csv("data.csv", header=None)
    df.columns = ["title", "description"]

    db = EndeeDB()

    for _, row in df.iterrows():
        text = row["title"] + " " + row["description"]

        emb = get_embedding(text)
        db.add(text, emb)

    return db


db = load_db()
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.lower()



# UI Styling Section

st.markdown("""
<style>

/* Background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1608889175123-8ee362201f81");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Dark Overlay */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.75);
}

/* Content */
.main {
    position: relative;
    z-index: 1;
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #FFD700;
    margin-top: 40px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #ccc;
    margin-bottom: 30px;
}

/* Search box */
div.stTextInput {
    max-width: 400px;
    margin: auto;
}

div.stTextInput input {
    height: 35px;
    font-size: 14px;
}

/* Movie Cards */
.movie-card {
    padding: 15px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    text-align: center;
    transition: 0.3s;
}

.movie-card:hover {
    transform: scale(1.05);
    background: rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)


# Title Section

st.markdown('<div class="title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Search movies by mood, genre, or name</div>', unsafe_allow_html=True)


# Search Input Section

query = st.text_input("🔍 Search for movies")


# Recommendations Section

if query:
    query_emb = get_embedding(query)
    results = db.search(query_emb, top_k=8)

    st.subheader("🎯 Recommended Movies")

    cols = st.columns(4)

    for i, (movie, score) in enumerate(results):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="movie-card">
                    <h4>{movie}</h4>
                    <p>⭐ {round(score, 2)}</p>
                </div>
            """, unsafe_allow_html=True)
