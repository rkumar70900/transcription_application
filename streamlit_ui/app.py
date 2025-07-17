import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
logs = client.transcriptions.logs

st.title("📝 Daily Logs")

entries = list(logs.find())

for log in entries:
    st.subheader(log['title'])
    st.audio(f"/mnt/pen_drive/{log['filename']}", format="audio/wav")
    with st.expander("Transcript"):
        st.write(log['transcript'])