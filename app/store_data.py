from pymongo import MongoClient
import uuid
import os
from datetime import datetime
import pytz

#mongodb-localhost

cst = pytz.timezone('US/Central')

client = MongoClient("mongodb://mongodb:27017/")
db = client.transcriptions

def store_transcription(file_path, transcript, title):
    data = {
        "uuid": str(uuid.uuid4()),
        "filename": os.path.basename(file_path),
        "transcript": transcript,
        "title": title,
        "created_at": datetime.now(cst),
        "updated_at": datetime.now(cst)
    }
    db.logs.insert_one(data)
    return data

def update_transcript(transcript_id: str, new_transcript: str, new_title: str):
    result = db.logs.update_one(
        {"uuid": transcript_id},
        {"$set": {"transcript": new_transcript, "title": new_title, "updated_at": datetime.now(cst)}},
        upsert=True
    )
    print(result)
    return result

def get_all_transcripts():
    transcripts = []
    for doc in db.logs.find():
        doc['_id'] = str(doc['_id'])
        transcripts.append(doc)
    return transcripts
    