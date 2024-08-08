import os
import yt_dlp
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment

def download_youtube_video(url, download_path):
    # Ensure the download directory exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'best'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded video to {download_path}")
    except yt_dlp.utils.DownloadError as e:
        print(f"An error occurred: {e}")

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)
    
    with audio_file as source:
        audio = recognizer.record(source)
        
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Audio not clear enough to transcribe"
    except sr.RequestError:
        return "Could not request results; check your network connection"

def extract_words(text):
    words = text.split()
    unique_words = list(set(words))
    return unique_words

# Example usage
video_url = 'https://www.youtube.com/watch?v=9vd5kyaRTDY'
download_path = 'C:\\Users\\Sruthi\\Downloads\\video'
video_file_path = os.path.join(download_path, 'video_file.mp4')
audio_file_path = os.path.join(download_path, 'audio_file.wav')

# Step 1: Download the video
download_youtube_video(video_url, download_path)

# Step 2: Extract audio from the video
extract_audio(video_file_path, audio_file_path)

# Step 3: Transcribe the audio to text
transcript = transcribe_audio(audio_file_path)
print("Transcript:", transcript)

# Step 4: Extract words from the transcribed text
words = extract_words(transcript)
print("Extracted Words:", words)
