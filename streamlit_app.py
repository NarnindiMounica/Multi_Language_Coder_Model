import streamlit as st
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Mario Mouni Model", page_icon="👨‍🦰")
st.title("👨‍🦰Coder Mario")

model = OllamaLLM(model='Mouni_Mario')
question=st.text_input("Ask your question please")

if question:
    st.success(model.invoke(question))

