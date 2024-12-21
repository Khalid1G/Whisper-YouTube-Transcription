import os
import tempfile
import time
import re
import librosa
from yt_dlp import YoutubeDL
import whisper

whisper_model = whisper.load_model("base")

# Define the YouTube video URL
YT_ID = input("set your youtube video ID: ")
YOUTUBE_VIDEO = f"https://www.youtube.com/watch?v={YT_ID}"
# Check if the transcription already exists
if not os.path.exists(f"Youtube/{YT_ID}_transcription.txt"):
    # Download the audio using yt-dlp
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_file_path = os.path.join(tmpdir, "audio.mp3")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(tmpdir, "audio.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([YOUTUBE_VIDEO])

        # Fix the filename based on how yt-dlp processes it
        if not os.path.exists(audio_file_path):
            audio_file_path = audio_file_path + ".mp3"
            if not os.path.exists(audio_file_path):
                raise FileNotFoundError(f"Audio file not found at {audio_file_path}")

        # Get the duration of the audio file
        duration = librosa.get_duration(path=audio_file_path)
        print("Video length:", duration, "seconds")

        # Transcribe the audio
        start = time.time()
        result = whisper_model.transcribe(audio_file_path, fp16=False)
        end = time.time()
        seconds = end - start
        print("Transcription time:", seconds)

        # Format the transcription
        sentences = re.split("([!?.])", result["text"])
        sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])]
        text = "\n".join(sentences)

        # Save the transcription to a file
        with open(f"Youtube/{YT_ID}_transcription.txt", "w") as file:
            file.write(text)

        print("\n\n", "-" * 100, "\n\nYour transcript is here: transcription.txt")
