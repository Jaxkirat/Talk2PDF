import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os
import openai

# Sidebar contents
with st.sidebar:
    st.title('Talk2PDF')
    st.markdown('''
    ## About
    This app is a Chatbot that can be used to read custom PDFs - Hence the name, Talk2PDF. 
    It uses a Retrieval Augmentation Model (RAG) to get the information from the PDF uploaded by the user(You😄).
    
    This app is made by using the following technologies:

    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    ''')
    add_vertical_space(5)
    st.write('Created by :  - [Jaskirat Singh ](https://Github.com/Jaxkirat)')

load_dotenv()

def main():
    st.header("Talk2PDF - Interact with you PDF")

    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        try:
            pdf_reader = PdfReader(pdf)
            
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            if not text.strip():
                st.error("No text found in the PDF file.")
                return

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text=text)

            store_name = pdf.name[:-4]
            st.write(f'Processing PDF: {store_name}')
            
            embeddings = OpenAIEmbeddings()

            if os.path.exists(f"{store_name}.faiss"):
                VectorStore = FAISS.load_local(f"{store_name}.faiss", embeddings, allow_dangerous_deserialization=True)
                st.write('Embeddings Loaded from Disk')
            else:
                VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
                VectorStore.save_local(f"{store_name}.faiss")

            query = st.text_input("Ask questions about your PDF file:")

            if query:
                docs = VectorStore.similarity_search(query=query, k=3)

                llm = OpenAI()
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=query)
                    print(cb)
                st.write(response)

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
