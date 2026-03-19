# Movie Recommendation System using Endee Vector Database

## Overview
This project is based on AI powered movie recommendation system that uses semantic search to recommend movies according to user input.

## Tech Stack
1. Python
2. Streamlit
3. Sentence Transformers
4. Endee Vector Database

## How It Works
1. Movie descriptions are converted into embeddings using Sentence Transformers
2. Embeddings are stored in Endee (vector database)
3. User query is also converted into embedding
4. Similarity search is performed using Endee
5. Top matching movies are returned

## Features
1. Semantic search
2. AI based recommendations
3. Vector similarity matching
4. Real time UI using Streamlit

## Endee Usage
Endee is used as a vector database concept for storing embeddings and performing semantic similarity search.


## UI Overview
<img width="1919" height="1027" alt="Screenshot 2026-03-19 152218" src="https://github.com/user-attachments/assets/8df5388c-6126-49e0-8280-f4d050debd35" />


## How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

# run command in proper directory
cd "C:\Endee Project\MovieRec"
streamlit run app.py
