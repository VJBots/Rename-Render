# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21006440")

API_HASH = os.environ.get("API_HASH", "f3b3fae13d20ab4b5f34ac3475749c20")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6857769889:AAGjEBSZ0WC1f2jy_IRxKeMpfgGH_7HCugM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "vastvikbot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevastvikbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://durgeshp28531:<ZstKrMiKDAJaMuR4>@cluster0.pqdxdob.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/84a592985d0ebda914884.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6277856017').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
