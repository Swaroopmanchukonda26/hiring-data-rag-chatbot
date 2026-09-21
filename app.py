import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.llm = Groq(model="openai/gpt-oss-20b", api_key=st.secrets["GROQ_API_KEY"])
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

st.title("Ask My Hiring Data")

@st.cache_resource
def load_index():
    documents = SimpleDirectoryReader(input_files=["real_data.txt"]).load_data()
    return VectorStoreIndex.from_documents(documents)

index = load_index()
query_engine = index.as_query_engine()

question = st.text_input("Ask a question about the hiring/layoffs data:")

if question:
    response = query_engine.query(question)
    st.write(response.response)