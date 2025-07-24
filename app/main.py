from fastapi import FastAPI
from read_files import get_audio_files
from transcribe import transcribe_audio
from store_data import store_transcription, update_transcript, get_all_transcripts
from models import TranscriptUpdate
from fastapi.exceptions import HTTPException
from ask_llm import llm_title

app = FastAPI()

@app.post("/process/")
async def process_audio():
    files = get_audio_files("/mnt/pen_drive")
    results = []
    for file in files:
        transcript = transcribe_audio(file)
        title = llm_title(transcript)
        result = store_transcription(file, transcript, title)
        results.append(result)
    return {"message": "Audio processed successfully"}

@app.put("/update_transcript/")
async def update_transcript_route(data: TranscriptUpdate):
    result = update_transcript(data.transcript_id, data.new_transcript, data.new_title)
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Transcript not found or not updated")
    return {"status": "success"}

@app.get("/transcripts")
async def get_transcripts():
    return {"transcripts": get_all_transcripts()}

@app.get("/title")
def title(transcript_text: str):
    return {"title": llm_title(transcript_text)}

