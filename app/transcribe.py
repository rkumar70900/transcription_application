import whisper

model = whisper.load_model("small")

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    transcript = result['text']
    title = transcript.split('.')[0][:50]  # First sentence or 50 chars
    return transcript, title