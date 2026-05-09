import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# LOAD DATASET
# ==============================

file_path = r"C:\Users\Niruban\Documents\Suriya\HCLGUVI\movie_recommendation_project\full_movies_2024.csv"

df = pd.read_csv(file_path)

# ==============================
# BASIC CLEANING
# ==============================

# Fill missing values
df['Storyline'] = df['Storyline'].fillna('')
#df['Genre'] = df['Genre'].fillna('')
df['Rating'] = df['Rating'].fillna(0)

# Convert rating into numeric
df['Rating'] = pd.to_numeric(df['Rating'],errors='coerce').fillna(0)

# Text Cleaning Function
def clean_text(text):

    text = str(text).lower()

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    return text

# Create Clean Columns
df['Clean_Story'] = df['Storyline'].apply(clean_text)

#f['Clean_Genre'] = df['Genre'].apply(clean_text)



# ==============================
# TF-IDF VECTORIZATION
# ==============================

tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(df['Clean_Story'])

# ==============================
# RECOMMENDATION FUNCTION
# ==============================

def recommend_movies(user_input, top_n=5):

    # Clean User Input
    cleaned_input = clean_text(user_input)

    # Convert User Input into Vector
    user_vector = tfidf.transform([cleaned_input])

    # Calculate Cosine Similarity
    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    ).flatten()

    # Add Similarity Score
    df['Similarity'] = similarity_scores

    # Sort Based On:
    # 1. Similarity
    # 2. Rating

    #recommendations = df.sort_values(by=['Similarity', 'Rating'],ascending=False).head(top_n)
    recommendations = df.sort_values(by=['Similarity'],ascending=False).head(top_n)

    # Return Important Columns
    return recommendations[['Movie Name','Storyline','Rating','Similarity']]
    #return recommendations[['Movie Name','Storyline','Similarity']]