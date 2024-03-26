import streamlit as st
import base64

from streamlit_card import card
from streamlit_extras.app_logo import add_logo
from Methods import Methods as mtd
from Constants import Constants as ct


def main():
    res = card(
        title="RECOM_AI",
        text="AI-powered Movie/TV series recommender",
        image="https://iili.io/Jjzq2aa.jpg",
        styles={
            "card": {
                "width": "100%",
                "height": "300px",
            }
        }
    )   
    add_logo("logo.png",120)
    
    
if __name__ == "__main__":
    main()