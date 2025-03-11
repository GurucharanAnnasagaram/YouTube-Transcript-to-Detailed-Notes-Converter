Key Features:
✅ YouTube Transcript Extraction – Retrieves text from YouTube videos.
✅ AI-Powered Summarization – Uses Google Gemini-Pro to summarize transcripts within 250 words.
✅ Automatic Thumbnail Display – Displays the video thumbnail for better UX.
✅ Streamlit-Based UI – Users can input a video link and get a summarized version.

Technology Stack:
Streamlit – Builds an interactive web interface.
YouTube Transcript API – Extracts subtitles/transcripts.
Google Generative AI (Gemini-Pro) – Summarizes video content.
dotenv – Securely loads API keys.
How It Works:
User inputs a YouTube video link.
The app extracts the transcript using YouTubeTranscriptApi.
Gemini-Pro generates a concise summary of the video.
The summarized notes are displayed in an easy-to-read format.
