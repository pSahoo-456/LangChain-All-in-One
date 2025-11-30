import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter=RecursiveCharacterTextSplitter(
        #separators=["\n\n", "\n", " ", ""],
        chunk_size=1000,
        chunk_overlap=1000,
        #length_function=len
    )
    chunks=text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore=FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    vectorstore.save_local("faiss_index")
    return vectorstore

def get_conversation_chain(vectorstore):
    prompt_template="""You are a helpful AI assistant. Use the following context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    {context}
    Question: {question}
    Answer in detail:"""

    model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)

    PROMPT=PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
    chain=load_qa_chain(model,chain_type="stuff",prompt=PROMPT)
    return chain


def user_input(user_question):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    new_db=FAISS.load_local("faiss_index",embeddings, allow_dangerous_deserialization=True)
    docs=new_db.similarity_search(user_question)

    chain=get_conversation_chain(docs)  # Pass docs to the function

    response=chain(
        {"input_documents":docs,"question":user_question}
        ,return_only_outputs=True
    )   
       
    print(response)
    st.write("Reply:",response['output_text'])


def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini≡ƒÆü")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vectorstore(text_chunks)
                st.success("Done")


if __name__ == "__main__":
    main()
