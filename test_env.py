from dotenv import load_dotenv
import os

load_dotenv()
print("API Token:", os.getenv("API_TOKEN"))
