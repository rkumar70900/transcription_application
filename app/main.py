from fastapi import FastAPI
from read_files import get_audio_files
from transcribe import transcribe_audio
from store_data import store_transcription, update_transcript, get_all_transcripts
from models import TranscriptUpdate
from fastapi.exceptions import HTTPException


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

@app.put("/update_transcript/")
async def update_transcript_route(data: TranscriptUpdate):
    result = update_transcript(data.transcript_id, data.new_transcript)
    print(result)
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Transcript not found or not updated")
    return {"status": "success"}

@app.get("/transcripts")
async def get_transcripts():
    return {"transcripts": get_all_transcripts()}

