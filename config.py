import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27639102")

API_HASH = os.environ.get("API_HASH", "35142c1407be6264e68fb6bec5dcabd9")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5994040795:AAFoT79XfcpecrbkWOX6raSt9KRQ9InUYyg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Bots") 

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://VJlink:VJLink@cluster0.ucnckh4.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")
