import whisper

model = whisper.load_model("small")

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    transcript = result['text']
    return transcript