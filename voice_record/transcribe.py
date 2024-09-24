import whisper

# Load Whisper model
model = whisper.load_model("large")

# Audio file
wav_file = "voice_record_converted_mono.wav"

# Transcribe the WAV file
result = model.transcribe(wav_file)

# Save the transcription to a text file
output_file = "transcription.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(result["text"])
