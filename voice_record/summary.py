from transformers import pipeline

# Summarization model, such as BART
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Loade the transcription from a file
with open("transcription.txt", "r", encoding="utf-8") as f:
    transcription_text = f.read()

# Generate a summary with the more advanced model
summary = summarizer(transcription_text, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]

# Save the summary to a file
with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)
