# utils/gemini_client.py
import os 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() 

genai.configure(api_key=os.getenv("AGENT_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def generate_response(conversation):
    messages = [
        {"role": "user", "parts": msg} if role == "user" else {"role": "model", "parts": msg}
        for role, msg in conversation
    ]
    chat = model.start_chat(history=messages)
    response = chat.send_message(conversation[-1][1])
    return response.text
