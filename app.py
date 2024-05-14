import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import time

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_template = """
You are an expert in recommending hiking trails based on the season and city.
Provide the top 5 hiking trails for the given season and city.
Include a brief description of each trail, its difficulty level, and any notable features.

Season: {season}
City: {city}
"""

def generate_content(season, city):
    response = model.generate_content(prompt_template.format(season=season, city=city))
    return response.text

def stream_output(reply):
    for word in reply.split(" "):
        yield word + " "
        time.sleep(0.02)

st.title("Top 5 Hiking Trails Recommendation")

c1, c2 = st.columns(2)

with c1:
    season = st.selectbox("Select the season", ["Spring", "Summer", "Fall", "Winter"])

with c2:
    city = st.text_input("Enter the city")

reply = None

if st.button("Get Hiking Trails Recommendations", use_container_width=True):
    reply = generate_content(season, city)
    st.write(reply)
