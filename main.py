import os
from dotenv import load_dotenv
load_dotenv()

#Adding our API Key safely
api_key = os.getenv('API_KEY')