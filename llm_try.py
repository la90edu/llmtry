from openai import OpenAI
client = OpenAI()
import streamlit as st

def return_answer():
 prompt = (
    "give me a nice welcome"
)
 response = client.chat.completions.create(
 model="gpt-4o",
 messages=[{"role":"user","content":prompt}]
 )
 return response.choices[0].message.content.strip()



response=return_answer()
st.write(response)
