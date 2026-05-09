# 🎬 Movie Recommendation System

A professional Movie Recommendation System built using Python, IMDb movie data, Machine Learning, and Streamlit.

This project recommends similar movies based on movie storyline and textual similarity using TF-IDF Vectorization and Cosine Similarity.

# 🚀 Features
- IMDb movie data scraping using Selenium
- Data preprocessing using Pandas
- Content-based movie recommendation
- TF-IDF text vectorization
- Cosine Similarity recommendation engine
- Interactive Streamlit web application
- Search movies instantly
- Top 5 similar movie recommendations
- Clean and responsive UI


# 🛠️ Technologies Used
## Programming Language
- Python

## Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Selenium
- Streamlit

## Machine Learning Techniques
- TF-IDF Vectorization
- Cosine Similarity

## Web Scraping
- Selenium WebDriver
- IMDb Dataset Extraction

## Frontend/UI
- Streamlit

## Development Tools
- VS Code
- Jupyter Notebook

---

# 📂 Project Structure

movie_recommendation_project/

├── data/

│   └── full_movies_2024.csv

├──recommendation_engine

├── test.py

├── streamlitapp.py

├── README.md

---

# ⚙️ How It Works

## Step 1 — Data Collection
Movie data is collected from IMDb using Selenium web scraping.

Collected information:
- Movie Name
- Storyline
- Rating

## Step 2 — Data Cleaning
The dataset is cleaned using Pandas:
- Remove null values
- Remove duplicates
- Text preprocessing


## Step 3 — Feature Engineering
Movie storylines are converted into numerical vectors using:

- TF-IDF Vectorizer

## Step 4 — Similarity Calculation
Cosine Similarity is used to calculate similarity between movies.


## Step 5 — Recommendation
When the user selects a movie, the system recommends top similar movies.

# 🧠 Machine Learning Concept Used

## TF-IDF Vectorization
TF-IDF converts movie storyline text into numerical vectors.

## Cosine Similarity
Measures similarity between movie vectors.
Movies with higher cosine similarity are recommended.

# ▶️ Run the Project

## Install Dependencies
```bash
pip install pandas scikit-learn streamlit selenium


NLP Technique Flow Diagram
User Story Input
        ↓
Text Cleaning
        ↓
TF-IDF Vectorization
        ↓
Convert to Numerical Vector
        ↓
Cosine Similarity
        ↓
Find Similar Movies
        ↓
Top Recommendations
```bash
pip install pandas scikit-learn streamlit selenium
