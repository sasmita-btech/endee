from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)
    return chunks

def simulate_rag_query(chunks, query):
    print("\nQuery:", query)
    print("\nRetrieved Chunks:")

    for i, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {i+1}:")
        print(chunk.page_content[:200])

if __name__ == "__main__":
    print("AI Semantic Search using Endee (RAG Demo)")

    try:
        chunks = load_and_split_pdf("sample.pdf")
        print(f"PDF processed into {len(chunks)} chunks")

        user_query = "What is this document about?"
        simulate_rag_query(chunks, user_query)

    except:
        print("Error: Add sample.pdf file")
