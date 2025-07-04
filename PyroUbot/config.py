import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "919211317").split()))

API_ID = int(os.getenv("API_ID", "21853004"))

API_HASH = os.getenv("API_HASH", "109a605351c0c15cd7235fa13df60066")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8086835207:AAEIRt3hEH2uO7feeyNa2ZtqoPp9zJHir_I")

OWNER_ID = int(os.getenv("OWNER_ID", "919211317"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ubotneewwee:Ubotneewwee@ubotneewwee.56zajtg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002312835928"))
