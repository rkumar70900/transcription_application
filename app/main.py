from fastapi import FastAPI
from read_files import get_audio_files
from transcribe import transcribe_audio
from store_data import store_transcription

app = FastAPI()

@app.post("/process/")
async def process_audio():
    files = get_audio_files("/mnt/pen_drive")
    results = []
    for file in files:
        transcript, title = transcribe_audio(file)
        result = store_transcription(file, transcript, title)
        results.append(result)
    return {"message": "Audio processed successfully"}