import streamlit as st
import streamlit.components.v1 as components

from streamlit_card import card
from streamlit_extras.app_logo import add_logo
from Methods import Methods as mtd
from Constants import Constants as ct


def main():
    res = card(
        title="RECOM_AI",
        text=["AI-powered Movie/TV series recommender","Leveraging AI for personalized recommendations"],
        image="https://th.bing.com/th/id/OIG2.SwJHNmgi9PsKpb523IxC?pid=ImgGn",
        styles={
            "card": {
                "width": "100%",
                "height": "400px",
            }
        }
    )   
    add_logo("logo.png",150)
    with st.container(border=True):
        st.header("What does it do?")
        st.subheader('🍿Recommend by similarity',divider=True,anchor=False)
        st.write("""Helps you generate recommendations of Movie/TV show that
                 are similar in terms of many aspects to the specific Movie/TV series given and tailoring to your likings.
                """)
        st.subheader('🎭Recommend by genre',divider=True,anchor=False)
        st.write("""Helps you generate recommendations of Movie/TV show based on the genre and keywords given.
                """)
        st.subheader('🔀Random recommendation',divider=True,anchor=False)
        st.write("""Generate random recommendations of Movie/TV show to help you discover new hits or hidden gems, 
                 that you can add to your watch list.
                """)
    
if __name__ == "__main__":
    main()