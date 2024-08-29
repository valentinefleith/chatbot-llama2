from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

st.title("Langchain Chatbot With LLama2 model")
input_text = st.text_input("Ask your question!")

llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the questions"),
        ("user", "Question:{question}"),
    ]
)

chain = prompt | llm

if input_text:
    st.write(chain.invoke({"question": input_text}))
