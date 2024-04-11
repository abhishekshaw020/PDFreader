import streamlit as st
import pyttsx3
import fitz  # PyMuPDF
import base64
from io import BytesIO

def text_to_speech(text):
    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()
    # Set properties before adding anything to say
    speaker.setProperty('rate', 150)  # Speed of speech
    speaker.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    # Save the speech to an audio file
    speech_buffer = BytesIO()
    speaker.save_to_buffer(text, speech_buffer)
    speech_buffer.seek(0)
    return speech_buffer

def pdf_to_text(uploaded_file):
    # Read the uploaded file as bytes
    pdf_bytes = BytesIO(uploaded_file.read())
    # Open the PDF file
    pdf_document = fitz.open("pdf", pdf_bytes)
    num_pages = pdf_document.page_count

    # Extract text from each page
    text = ""
    for page_num in range(num_pages):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return text

def main():
    st.title("Audiobook by Abhishek Shaw")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Upload a PDF file")

    if uploaded_file is not None:
        # Convert the PDF to text
        text = pdf_to_text(uploaded_file)

        # Convert text to speech and get the audio file path
        audio_buffer = text_to_speech(text)

        # Convert audio buffer to base64
        audio_bytes = base64.b64encode(audio_buffer.getvalue()).decode('utf-8')

        # Display the audio file player
        st.audio(audio_bytes, format='audio/mp3')

if __name__ == "__main__":
    main()
