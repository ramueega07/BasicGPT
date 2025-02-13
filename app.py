import os
import requests
from apikey import apikey
from groq import Groq
import streamlit as st

os.environ["GROQ_API_KEY"]=apikey
client = Groq(api_key=os.environ.get("GROQ_API_KEY"), )

system_prompt = {
    "role": "system",
    "content":
    "You are a helpful assistant. You reply with very meaningful answers."
}

chat_history=[system_prompt]
st.title('🦜️🔗 Auto GPT Creator')
prompt=st.text_input('Plug in your prompt')

chat_history.append({"role":"user","content":prompt})
response = client.chat.completions.create(model="llama3-70b-8192",messages=chat_history)
#llm = openai(temperature=0.9)

st.write( response.choices[0].message.content)