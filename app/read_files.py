import os

def get_audio_files(directory: str):
    supported_formats = ('.mp3', '.wav', '.m4a')
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(supported_formats)]