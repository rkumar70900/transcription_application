from pydantic import BaseModel

class LogItem(BaseModel):
    uuid: str
    filename: str
    transcript: str
    title: str

class TranscriptUpdate(BaseModel):
    transcript_id: str
    new_title: str | None = None
    new_transcript: str | None = None