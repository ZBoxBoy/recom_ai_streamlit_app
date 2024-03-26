import streamlit as st
import time

from streamlit_extras.app_logo import add_logo
from Methods import Methods as mtd

add_logo("logo.png",120)

#Page title
st.title("Generate the best movie/series recommendations from your favorite genre.🎭",anchor=False)
st.divider()

submitted = False

#Multiselect options for genre(s)
options = st.sidebar.multiselect(
                        'Genre:',
                        [
                        'Action',
                        'Adventure',
                        'Animation',
                        'Comedy',
                        'Crime',
                        'Documentary',
                        'Drama',
                        'Family',
                        'Fantasy',
                        'Film Noir',
                        'Game Show',
                        'Historical',
                        'Horror',
                        'Musical',
                        'Music',
                        'Mystery',
                        'Romance',
                        'Sci-fi',
                        'Short',
                        'Sport',
                        'Supernatural',
                        'Thriller',
                        'War',
                        'Western'
                        ],
                        ["Sci-fi","Action"],
                        max_selections=3,
                        help="""
                        Choose the genre of the Movie/Series to be recommended (max 3). 
                        Note that not all of the generated recommendation will have all selected genre(s).""")

#Text area for user's keywords
keywords = st.sidebar.text_area(
"What would you like to see?",
"Futuristic world, alien invasion, superhumans, action packed",
max_chars=200, help="""Keywords describing the characteristic or element of movies/series (seperated with commas if multiple) 
                        that you want the recommendations to have.
                        E.g. "beautiful environments", "action packed", "high-stakes", etc.
                        """,placeholder="(Optional)")

#Radio button for recommendation type
type = st.sidebar.radio(
    "Recommendation type",
    ("Movie", "Series", "Both"),
    horizontal=True,
    help="Choose the entertainment type that you want the recommendation to be generated by.")

#Max amount of output
max = st.sidebar.slider('Max recommendation', 1, 10, 5,
                help="Pick the maximum amount of recommendation that you want to be generated.")

#Submit button
if st.sidebar.button('Generate',use_container_width=True):
    is_empty = len(options) == 0
    if is_empty:
        alert = st.sidebar.warning('Genre selection field is empty', icon="⚠️")
        time.sleep(3)
        alert.empty()
    else:
        st.toast('Submitted for generation...')
        if keywords == "":
            keywords = "The best in the genre"
        with st.spinner('Generating recommendations, please wait... 🍵'):
            time.sleep(5)
            genre = ", ".join(options)
            recommendation = mtd.generate_genre(keywords,genre,type,max)
            if recommendation:
                submitted = True
                st.toast('Recommendations generated!')

#When submitted
if submitted:
    with st.expander("📃View as list"):
        list = "\n".join([f"{i+1}. {item}" for i, item in enumerate(recommendation)])
        st.write(list)
    for element in recommendation:
            parts = element.split(" (")
            t = parts[0]
            y = element[element.find("(")+1 : element.find(")")]
            data = mtd.getData(t,y)
            if data["Response"] == "True":
                if data["Poster"] == "N/A":
                    data["Poster"] = "https://www.reelviews.net/resources/img/default_poster.jpg"
                mtd.createComponent(
                data["Title"],
                data["Released"],
                data["imdbRating"],
                data["Poster"],
                data["Plot"],
                data["Type"],
                data["imdbID"],
                data["Director"],
                data["Genre"]
                )

    submitted = False

