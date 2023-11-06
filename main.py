import streamlit as st

# Title
st.title("Audio Player")

# Upload an audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

# Check if an audio file is uploaded
if audio_file is not None:
    # Display the audio player
    st.audio(audio_file, format='audio/*')
