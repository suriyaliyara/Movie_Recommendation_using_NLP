import streamlit as st

from recommendation_engine import recommend_movies

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title=" Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {background-color: #0e1117;color: white;}

.stButton>button {
    background-color: #f5c518;
    color: black;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}

.movie-card {
    background-color: #1f2937;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border-left: 5px solid #f5c518;
}

.rating {
    color: #f5c518;
    font-weight: bold;
    font-size: 18px;
}


.match {
    color: #00c8ff;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.title("🎬  Movie Recommendation System")

st.write("Enter a plot or mood, and we'll find 2024's best matches.")

# =====================================
# SIDEBAR
# =====================================

st.sidebar.header("🎥 About Project")

st.sidebar.info("""
This project recommends movies using:

- Storyline Similarity
- Rating 
- NLP Techniques

Technologies Used:
- Python
- Pandas
- Scikit-Learn
- Streamlit
""")

# =====================================
# USER INPUT
# =====================================

user_input = st.text_area("🎥 Enter Movie Storyline",placeholder="""Example:A magical wizard fighting dark powers
Sci-fi space thriller
Korean zombie action movie
Romantic comedy in college
"""
)

# Dynamic Slider
top_movies = st.slider(
    "Select Number of Recommendations",
    min_value=1,
    max_value=10,
    value=5
)

# =====================================
# BUTTON
# =====================================

if st.button("🔍 Recommend Movies"):

    if user_input.strip() != "":

        # Get Recommendations
        recommendations = recommend_movies(user_input,top_n=top_movies)

        st.subheader("🎬 Top Recommended Movies")

        # Display Recommendations
        for _, row in recommendations.iterrows():
           

            with st.container():

                st.write("---")

            col1, col2 = st.columns([4,1])

            with col1:
                st.subheader(f"🎬 {row['Movie Name']}")

            with col2:
                st.metric("⭐ Rating", row['Rating'])

            st.write("📖 Storyline")
            st.write(row['Storyline'])

            st.progress(float(row['Similarity']))

            st.write(
                f"🎯 Match Score: {round(row['Similarity'] * 100, 2)}%"
            )

        st.success(
            "✨ Explore more by trying different storylines g moods!"
        )

    else:
        st.warning(
            "⚠ Please enter a storyline or genre"
        )

