import streamlit as st
import time
from streamlit_extras.app_logo import add_logo
from Methods import Methods as mtd
from Constants import Constants as ct

def main():
    st.set_page_config(
        page_title="RECOM_AI",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    add_logo("logo.png",100)
    st.markdown(ct.PAGE_LAYOUT, unsafe_allow_html=True)
    col1, col2 = st.columns([3,7])
    with col1:
        st.image("logo.png",use_column_width=True)
    with col2:
        st.markdown("")
        st.subheader('AI-Powered Personalized movie/series recommender',anchor=False)
        st.write("Generate Movie/TV series title recommendations in a form of graphical and informative content.")
        st.caption("by Zakwan Zakkariya")

    st.markdown("")
    with st.expander('What does it do?'):
        st.header("It has 3 types of recommendations",anchor=False)
        st.markdown("")
        st.subheader('🍿Recommend by similarity',divider=True,anchor=False)
        st.write("""Helps you generate recommendations of Movie/TV show that
                 are similar in terms of many aspects to the specific Movie/TV series given and tailoring to your likings.
                """)
        st.markdown("")
        st.subheader('🎭Recommend by genre',divider=True,anchor=False)
        st.write("""Helps you generate recommendations of Movie/TV show based on the genre and keywords given.
                """)
        st.markdown("")
        st.subheader('🔀Random recommendation',divider=True,anchor=False)
        st.write("""Generate random recommendations of Movie/TV show to help you discover new hits or hidden gems, 
                 that you can add to your watch list.
                """)
    with st.expander("Output example"):
        coll1, coll2, coll3 = st.columns([0.2,0.6,0.2])
        with coll1:
            st.write("")
        with coll2:
            mtd.createExample(
                "Jurassic Park",
                "1993",
                "8.2",
                ct.JURASSIC_PARK_POSTER,
                ct.JURASSIC_PARK_PLOT,
                "Movie",
                "tt0107290",
                "Steven Spielberg",
                "Action, Adventure, Sci-Fi",
                "QWBKEmWWL38"
                )
        with coll3:
            st.write("")

if __name__ == "__main__":
    main()
