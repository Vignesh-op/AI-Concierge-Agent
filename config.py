import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def configure_gemini():
    """
    Reads GEMINI_API_KEY from the environment (.env) and configures the
    google-generativeai SDK. Call this before creating the agent.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY in environment. Add it to a .env file.")
    genai.configure(api_key=api_key)
    print("Gemini API configured successfully!")
