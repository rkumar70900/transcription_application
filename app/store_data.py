from pymongo import MongoClient
import uuid
import os

client = MongoClient("mongodb://mongodb:27017/")
db = client.transcriptions

def store_transcription(file_path, transcript, title):
    data = {
        "uuid": str(uuid.uuid4()),
        "filename": os.path.basename(file_path),
        "transcript": transcript,
        "title": title
    }
    db.logs.insert_one(data)
    return data