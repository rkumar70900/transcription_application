from pydantic import BaseModel

class LogItem(BaseModel):
    uuid: str
    filename: str
    transcript: str
    title: str