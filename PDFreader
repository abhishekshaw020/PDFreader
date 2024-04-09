import streamlit as st
import pyttsx3
import fitz  # PyMuPDF
import pickle
from io import BytesIO

def text_to_speech(text):
    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()
    # Set properties before adding anything to say
    speaker.setProperty('rate', 150)  # Speed of speech
    speaker.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    # Save the speech to an audio file
    speaker.save_to_file(text, 'speech.mp3')
    speaker.runAndWait()
    # Return the path to the audio file
    return 'speech.mp3'

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
    st.title("PDF to Audio Converter")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Upload a PDF file")

    if uploaded_file is not None:
        # Convert the PDF to text
        text = pdf_to_text(uploaded_file)
        
        # Save text to a pickle file
        with open("text.pickle", "wb") as f:
            pickle.dump(text, f)

        # Convert text to speech and get the audio file path
        audio_file = text_to_speech(text)

        # Display the audio file player
        st.audio(audio_file)

if __name__ == "__main__":
    main()
