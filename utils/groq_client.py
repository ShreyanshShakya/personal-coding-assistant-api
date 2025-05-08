import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

def get_groq_client():
    """Initialize and return the Groq client."""
    api_key = os.environ.get("GROQ_API_KEY")
    print(f"Loaded API Key")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    return Groq(api_key=api_key)