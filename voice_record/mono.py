from pydub import AudioSegment

# Path to the files
wav_file = "voice_record_converted.wav"
mono_wav_file = "voice_record_converted_mono.wav"

# Load the WAV file
audio = AudioSegment.from_wav(wav_file)

# Convert to mono
audio_mono = audio.set_channels(1)

# New WAV file
audio_mono.export(mono_wav_file, format="wav")
