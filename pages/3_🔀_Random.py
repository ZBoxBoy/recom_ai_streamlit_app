import streamlit as st
import time

from streamlit_extras.app_logo import add_logo
from Methods import Methods as mtd
from Constants import Constants as ct

st.set_page_config(
    page_title="Random recommendation",
    page_icon="🔀",
    layout="wide",
    initial_sidebar_state="expanded",
)
add_logo("logo.png",210)
# st.markdown(ct.PAGE_LAYOUT, unsafe_allow_html=True)

#Page title
st.title("Generate random movie/series for new discovery.🔀",anchor=False)
st.divider()

submitted = False

category = st.sidebar.radio(
    "Pick your poison",
    ("Popular", "Underrated","Any"),
    horizontal=True,
    help="Choose the category that you want the recommendation to be generated by.")

#Max amount of output
max = st.sidebar.slider('Max recommendation', 1, 10, 5,
                help="Pick the maximum amount of recommendation that you want to be generated.")

#Radio button for recommendation type
type = st.sidebar.radio(
    "Recommendation type",
    ("Movie", "Series", "Both"),
    horizontal=True,
    help="Choose the entertainment type that you want the recommendation to be generated by.")

#Submit button
if st.sidebar.button('Generate',use_container_width=True):
    with st.spinner('Generating recommendations, please wait... 🍵'):
        st.toast('Submitted for generation...')
        time.sleep(5)
        recommendation = mtd.generate_random(category,type,max)
        if recommendation:
            submitted = True
            st.toast('Recommendations generated!')

#When submitted
if submitted:
    mtd.mainOutput(recommendation)
