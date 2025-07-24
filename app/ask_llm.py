from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def llm_title(transcript, model="gpt-3.5-turbo"):

    user_query = f"Generate a short, descriptive title for the following transcript:\n\n{transcript}"
    
    messages = [
        {"role": "system", "content": "You are a creative assistant, that can generate a short, descriptive title for a given transcript."},
        {"role": "user", "content": f"Question: {user_query}"}
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )
    
    response = str(response.choices[0].message.content)
    return response