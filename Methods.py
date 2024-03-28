import streamlit as st
import urllib.parse
import requests
import json
import streamlit.components.v1 as components
import time

from openai import OpenAI
from Constants import Constants as ct

class Methods:
    
    def ai_generate(system_prompt, user1, assistant1, user2, assistant2, user3, assistant3, user_prompt):
        openai = OpenAI(api_key = st.secrets.OPENAI_API_KEY)
        response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system",
             "content":system_prompt},
            {"role":"user",
              "content":user1},
            {"role":"assistant",
              "content":assistant1},
            {"role":"user",
              "content":user2},
            {"role":"assistant",
              "content":assistant2},
            {"role":"user",
              "content":user3},
            {"role":"assistant",
              "content":assistant3},
            {"role":"user",
              "content":user_prompt}
        ],
        max_tokens=750
        )
        recommendations = response.choices[0].message.content
        return recommendations
    
    #Generate recommendation by similarity
    def generate_similarity(title,interest,type,max):
        if type == "Both":
            type = "Movie or Series"
        s = ct.SIM_SYS_PROMPT
        u1 = ct.SIM_USER1
        a1 = ct.SIM_ASSISTANT1
        u2 = ct.SIM_USER2
        a2 = ct.SIM_ASSISTANT2
        u3 = ct.SIM_USER3
        a3 = ct.SIM_ASSISTANT3
        prompt = f"""
        Title: {title}\
        Likings: {interest}\
        Type: {type}
        Max: {max}
        """
        recommendation = json.loads(Methods.ai_generate(s,u1,a1,u2,a2,u3,a3,prompt))
        return recommendation

    #Generate recommendation by genre
    def generate_genre(keywords,genre,type,max):
        if type == "Both":
            type = "Movie or Series"
        s = ct.GENRE_SYS_PROMPT
        u1 = ct.GENRE_USER1
        a1 = ct.GENRE_ASSISTANT1
        u2 = ct.GENRE_USER2
        a2 = ct.GENRE_ASSISTANT2
        u3 = ct.GENRE_USER3
        a3 = ct.GENRE_ASSISTANT3
        prompt = f"""
        Keywords: {keywords}
        Genre: {genre}
        Type: {type}
        Max: {max}
        """
        recommendation = json.loads(Methods.ai_generate(s,u1,a1,u2,a2,u3,a3,prompt))
        return recommendation
    
    #Generate random
    def generate_random(category,type,max):
        if type == "Both":
            type = "Movie or Series"
        if category == "Any":
            category = "Known or less known"
        s = ct.RAND_SYS_PROMPT
        u1 = ct.RAND_USER1
        a1 = ct.RAND_ASSISTANT1
        u2 = ct.RAND_USER2
        a2 = ct.RAND_ASSISTANT2
        u3 = ct.RAND_USER3
        a3 = ct.RAND_ASSISTANT3
        prompt = f"""
        Category: {category}
        Type: {type}
        Max: {max}
        """
        recommendation = json.loads(Methods.ai_generate(s,u1,a1,u2,a2,u3,a3,prompt))
        return recommendation

    #Get data method
    def getData(title, year):
        apikey = st.secrets.OMDb_API_KEY
        formatted = urllib.parse.quote(title)
        url = f'http://www.omdbapi.com/?t={formatted}&y={year}&apikey={apikey}'
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
        
        return json_data
    
    #Get youtube trailer
    def getYT(title, year):
        string = f'{title} ({year}) official trailer'
        q = urllib.parse.quote(string)
        key = st.secrets.YT_API_KEY
        url = ct.urlYT(key,q)
        response = requests.get(url)
        json_data = response.json()

        video_id = json_data["items"][0]["id"]["videoId"]
        return video_id

    #Create response component method
    def createComponent(name,year,rating,imageUrl,plot,type,id,director,genre):
        with st.container(border=True):
            st.header(f'{name} ({year})', anchor=False,divider=True)
            col1, col2= st.columns(2)  
            with col1:
                st.image(imageUrl,use_column_width=True,)
            with col2:
                st.write('📖Plot:')
                st.write(plot)
                st.markdown(f'📽️<b>Type: </b><i>{type.title()}</i>',unsafe_allow_html=True)  
                st.markdown(f'🎭<b>Genre: </b><i>{genre}</i>',unsafe_allow_html=True)
                st.markdown(f'🎬<b>Director: </b><i>{director}</i>',unsafe_allow_html=True)
                st.markdown(f'⭐<b>IMDb rating: </b><i>{rating}/10</i>',unsafe_allow_html=True)
            coll1, coll2= st.columns(2)
            with coll1:
                st.link_button("IMDb.com 🔗",f'https://www.imdb.com/title/{id}',use_container_width=True)
            with coll2:
                with st.popover('YouTube trailer 🎥',use_container_width=True):
                    ytId = Methods.getYT(name,year)
                    components.html(ct.ytEmbed(ytId),580,335)
                    
     #Create example component method
    def createExample(name,year,rating,imageUrl,plot,type,id,director,genre,ytId):
        with st.container(border=True):
            st.subheader(f'{name} ({year})',anchor=False,divider=True)
            col1, col2= st.columns(2)  
            with col1:
                st.image(imageUrl,use_column_width=True,)
            with col2:
                st.write('📖Plot:')
                st.write(plot)
                st.markdown(f'📽️<b>Type: </b><i>{type.title()}</i>',unsafe_allow_html=True)  
                st.markdown(f'🎭<b>Genre: </b><i>{genre}</i>',unsafe_allow_html=True)
                st.markdown(f'🎬<b>Director: </b><i>{director}</i>',unsafe_allow_html=True)
                st.markdown(f'⭐<b>IMDb rating: </b><i>{rating}/10</i>',unsafe_allow_html=True)
            coll1, coll2= st.columns(2)
            with coll1:
                st.link_button("IMDb.com 🔗",f'https://www.imdb.com/title/{id}',use_container_width=True)
            with coll2:
                with st.popover('YouTube trailer 🎥',use_container_width=True):
                    components.html(ct.ytEmbed(ytId),580,335)
                    
    #Main output method
    def mainOutput(recommendation):
        with st.expander("📃View as list"):
            list = "\n".join([f"{i+1}. {item}" for i, item in enumerate(recommendation)])
            st.write(list)
        count = 1
        done = False
        col1, col2 = st.columns(2)
        for element in recommendation:
                parts = element.split(" (")
                t = parts[0]
                y = element[element.find("(")+1 : element.find(")")]
                data = Methods.getData(t,y)
                if data["Response"] == "True":
                    if data["Poster"] == "N/A":
                        data["Poster"] = ct.DEFAULT_IMAGE
                    if count == 1:
                        with col1:
                            Methods.createComponent(
                            data["Title"],
                            y,
                            data["imdbRating"],
                            data["Poster"],
                            data["Plot"],
                            data["Type"],
                            data["imdbID"],
                            data["Director"],
                            data["Genre"]
                            )
                            count = 2
                            done = True

                    if count == 2 and done == False:
                        with col2:
                            Methods.createComponent(
                            data["Title"],
                            y,
                            data["imdbRating"],
                            data["Poster"],
                            data["Plot"],
                            data["Type"],
                            data["imdbID"],
                            data["Director"],
                            data["Genre"]
                            )
                            count =1

                    done = False
                    


