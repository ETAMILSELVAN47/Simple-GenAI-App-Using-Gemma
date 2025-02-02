import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

os.environ['LANGCHAIN_API_KEY']=os.getenv(key='LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']=os.getenv(key='LANGCHAIN_PROJECT')


#Prompt
prompt=ChatPromptTemplate.from_messages(
    [
        ('system','you are a helpful Assistant.Please respond to the questions asked.'),
        ('user','question:{question}')
    ]
)

#LLM
llm=Ollama(model="gemma:2b")

#Output parser
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

st.title('GenAI APP using Gemma')
input_text=st.text_input(label='What question you have in mind?')

if input_text:
    response=chain.invoke({'question':input_text})
    st.write(response)




