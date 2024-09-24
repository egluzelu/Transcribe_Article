from pydub import AudioSegment
import os

# Set the path to ffmpeg and ffprobe
ffmpeg_path = r"C:\Users\egluz\ffmpeg\ffmpeg.exe"
ffprobe_path = r"C:\Users\egluz\ffmpeg\ffprobe.exe"

# Set the environment variables for ffmpeg and ffprobe
os.environ["FFMPEG_EXECUTABLE"] = ffmpeg_path
os.environ["FFPROBE_EXECUTABLE"] = ffprobe_path

# Path to the files
mp3_file = "voice_record.mp3"
wav_file = "voice_record_converted.wav"

# Convert MP3 to WAV
audio = AudioSegment.from_mp3(mp3_file)
audio.export(wav_file, format="wav")
