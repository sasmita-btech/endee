import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

st.set_page_config(page_title="AI PDF Chatbot", layout="centered")

st.title("🤖 AI PDF Chatbot using Endee")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

def process_pdf(file):
    with open("temp.pdf", "wb") as f:
        f.write(file.read())

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    return chunks

if uploaded_file:
    chunks = process_pdf(uploaded_file)
    st.success(f"PDF processed into {len(chunks)} chunks")

    query = st.text_input("Ask a question:")

    if query:
        st.write("### 📄 Answer (Simulated RAG):")

        for i, chunk in enumerate(chunks[:3]):
            st.write(f"**Chunk {i+1}:**")
            st.write(chunk.page_content[:200])
