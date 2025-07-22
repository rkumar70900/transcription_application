import streamlit as st
import requests
import time
import ast

# Load transcripts from FastAPI
for i in range(10):
    try:
        response = requests.get("http://api:8000/transcripts")
        break
    except requests.exceptions.ConnectionError:
        time.sleep(2)

if response.status_code == 200:
    transcripts = response.json()
else:
    st.error("Could not load transcripts.")
    st.stop()

transcripts = transcripts['transcripts']

for transcript in transcripts:
    with st.expander(f"📄 {transcript['filename']}"):
        st.markdown(transcript["transcript"])

        if st.button(f"✏️ Edit - {transcript['uuid']}", key=f"edit_{transcript['uuid']}"):
            st.session_state[f"editing_{transcript['uuid']}"] = True

        if st.session_state.get(f"editing_{transcript['uuid']}", False):
            new_text = st.text_area(
                "Edit Transcript",
                value=transcript["transcript"],
                key=f"text_{transcript['uuid']}"
            )
            if st.button(f"✅ Submit - {transcript['uuid']}", key=f"submit_{transcript['uuid']}"):
                update_payload = {
                    "transcript_id": str(transcript["uuid"]),
                    "new_transcript": new_text
                }
                res = requests.put("http://api:8000/update_transcript/", json=update_payload)
                if res.status_code == 200:
                    st.success("Transcript updated!")
                    st.session_state[f"editing_{transcript['uuid']}"] = False
                else:
                    st.error("Failed to update transcript.")