from langchain.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs

if __name__ == "__main__":
    print("AI PDF Question Answering using Endee")

    file_path = "sample.pdf"   # keep a PDF in same folder
    try:
        documents = load_pdf(file_path)
        print("PDF Loaded Successfully!")
        print(f"Total Pages: {len(documents)}")
    except:
        print("Please add a PDF file named sample.pdf")
