from google import genai
from google.genai import types
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

st.title("GEMINI")
st.divider()

prompt = st.text_input("Prompt")
# submit = st.button("Submit")

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents=[prompt],
#      config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_level="low")
#     ),
# )
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt],
     config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)


st.markdown(response.text)



# st.write(response)