import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_documents():
    docs = []

    for file in os.listdir("knowledge_base"):
        path = os.path.join("knowledge_base", file)

        if file.endswith(".txt"):
            loader = TextLoader(path)
            docs.extend(loader.load())

    return docs


def split_documents(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    return chunks


def build_vector_database(chunks):

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local("vector_db")

    print("✅ Vector database built successfully.")


def main():

    print("Loading knowledge base documents...")

    docs = load_documents()

    print(f"Loaded {len(docs)} documents.")

    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks.")

    build_vector_database(chunks)


if __name__ == "__main__":
    main()