import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import time

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_content(prompt):
    response = model.generate_content(prompt)
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

additional_info = st.text_area("Additional Information (optional)", "")

reply = None
if st.button("Get Hiking Trails Recommendations", use_container_width=True):
    prompt = f"""
    You are an expert in recommending hiking trails based on the season and city.
    Provide the top 5 hiking trails for the given season and city.
    Include a brief description of each trail, its difficulty level, and any notable features.

    Season: {season}
    City: {city}

    Additional Information: {additional_info}

    Give the response in the following format:
    <response>
    1. Trail Name:
       Description:
       Difficulty:
       Notable Features:

    2. Trail Name:
       Description:
       Difficulty:
       Notable Features:

    ...

    5. Trail Name:
       Description:
       Difficulty:
       Notable Features:
    </response>

    After providing the recommendations, generate a personalized message for the user based on the additional information provided.
    """
    reply = generate_content(prompt)

if reply:
    response_parts = reply.split("</response>")
    recommendations = response_parts[0].strip("<response>").strip()
    personalized_message = response_parts[1].strip() if len(response_parts) > 1 else ""

    st.write("Here are the top 5 hiking trails recommendations:")
    for trail_info in recommendations.split("\n\n"):
        with st.expander(trail_info.split("\n")[0].split(":")[1].strip()):
            st.write("\n".join(trail_info.split("\n")[1:]))

    if personalized_message:
        st.write("\nPersonalized Message:")
        st.write(personalized_message)

    st.write("\nHere are some additional resources for your hiking adventure:")
    resources_prompt = f"""
    Provide 3 relevant resources (websites, articles, or books) for hiking in {city} during {season}.
    """
    resources_reply = generate_content(resources_prompt)
    st.write(resources_reply)
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv
# import streamlit as st
# import time

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel('gemini-pro')

# prompt_template = """
# You are an expert in recommending hiking trails based on the season and city.
# Provide the top 5 hiking trails for the given season and city.
# Include a brief description of each trail, its difficulty level, and any notable features.

# Season: {season}
# City: {city}
# """

# def generate_content(season, city):
#     response = model.generate_content(prompt_template.format(season=season, city=city))
#     return response.text

# def stream_output(reply):
#     for word in reply.split(" "):
#         yield word + " "
#         time.sleep(0.02)

# st.title("Top 5 Hiking Trails Recommendation")

# c1, c2 = st.columns(2)

# with c1:
#     season = st.selectbox("Select the season", ["Spring", "Summer", "Fall", "Winter"])

# with c2:
#     city = st.text_input("Enter the city")

# reply = None

# if st.button("Get Hiking Trails Recommendations", use_container_width=True):
#     reply = generate_content(season, city)
#     st.write(reply)
