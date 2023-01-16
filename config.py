import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "17318541")

API_HASH = os.environ.get("API_HASH", "3f0136ab75eaa468e7b5f3020be17588")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5609721310:AAEo034QWlWz50WEbwIk-S53tplMOFe-VPw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001860403687") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://leecher-x:#DiViN143#@cluster0.e9vvmrg.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5328012377').split()]

PORT = os.environ.get("PORT", "8080")
