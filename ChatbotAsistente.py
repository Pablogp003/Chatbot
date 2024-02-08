import streamlit as st
from transformers import pipeline, set_seed
import logging
import sys
import fitz 


logging.basicConfig(filename='chatbot_usage.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

set_seed(42)
chat_pipeline = pipeline('text-generation', model='gpt2')

def extract_text_from_pdf(pdf_bytes):
    """
    Extracts text from a given PDF bytes.
    """
    text = ""
    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        st.error(f"An error occurred while processing the PDF: {e}")
    return text

def simulate_rag_function(query, pdf_text):
    """
    Generate a response based on the query using extracted PDF text for demonstration.
    This simplifies the usage of PDF content in responses.
    """
   
    if pdf_text:
        return pdf_text[:500]  
    else:
        return "Please upload a PDF document."

def log_interaction(query, response):
    """
    Log each interaction to simulate monitoring.
    """
    logging.info(f"User query: {query} - Chatbot response: {response}")

def chatbot_streamlit_ui():
    """
    Run the chatbot with a Streamlit web interface.
    """
    st.title("Software Development Assistant Chatbot")
    
    
    pdf_file = st.file_uploader("Upload a PDF document", type=['pdf'])
    pdf_text = ""
    if pdf_file is not None:
        pdf_bytes = pdf_file.getvalue()
        pdf_text = extract_text_from_pdf(pdf_bytes)
    
    user_input = st.text_input("Ask a question about software development:")
    if user_input:
        response = simulate_rag_function(user_input, pdf_text)
        log_interaction(user_input, response)
        st.text_area("Chatbot:", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    chatbot_streamlit_ui()