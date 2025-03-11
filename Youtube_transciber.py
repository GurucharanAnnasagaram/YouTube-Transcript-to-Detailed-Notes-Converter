import os
import streamlit as st
from dotenv import load_dotenv
from google.generativeai import configure, GenerativeModel
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()  # Load all env variables

# Configure Google Generative AI with the API key
configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for summarization
prompt = """You are Youtube video summarizer. You will be taking the transcript text and summarizing
the entire video and providing the important summary in points within 250 words. Please provide the summary
of the text given: """


# Function to extract transcript details from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for item in transcript_list:
            transcript += " " + item["text"]

        return transcript.strip()

    except Exception as e:
        raise e


# Function to generate content using Gemini
def generate_gemini_content(transcript_text, prompt):
    model = GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + transcript_text)
    return response.text


# Streamlit app setup
st.title("YouTube Transcript to Detailed Notes Converter")

# Input for YouTube video link
youtube_link = st.text_input("Enter YouTube video link")

# Display video thumbnail if link is provided
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to get detailed notes
if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes")
        st.write(summary)


