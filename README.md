# Hiring Data RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers natural-language questions about tech industry layoffs data - instead of clicking through static dashboard filters, you can just ask.

Live app: https://hiring-data-rag-chatbot-ytpbwfrqebbffxnfuoeewr.streamlit.app/

This project extends my earlier Tech Industry Hiring Intelligence Dashboard project, reusing the same layoffs dataset with a conversational, LLM-powered interface.

## What it does

Ask questions like:
- Which company had the most layoffs?
- What industry was hit hardest?
- Tell me everything about layoffs in this dataset

The app retrieves relevant facts from the dataset and uses an LLM to generate a natural-language answer, grounded in real data, not generic AI knowledge.

## Tech Stack

- Python - core language
- LlamaIndex - data indexing and retrieval (the R in RAG)
- Groq API - LLM for response generation (the G in RAG)
- HuggingFace Embeddings - free, local text embeddings
- Streamlit - web interface and deployment

## How it works

1. Raw layoffs data is summarized into key facts using Pandas
2. Facts are indexed into a searchable vector store using LlamaIndex
3. User questions are matched against the indexed facts
4. Relevant facts are passed to a Groq-hosted LLM to generate a natural-language answer

## Running locally

1. Clone this repo
2. Install dependencies: pip install -r requirements.txt
3. Add your Groq API key to .streamlit/secrets.toml as GROQ_API_KEY equals your key in quotes
4. Run: streamlit run app.py

## What I learned building this

My first hands-on project with LLMs, RAG, and vector search, including real debugging around model deprecations, dependency conflicts, and secure API key management for deployment.
