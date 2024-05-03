import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28536138")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "aaa6a5e298c71fa3a576a88b1a4c2b9b") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6830166477:AAE-V5K3P3AS84WVtuXTrAqrsBV8nkG-eMs") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'thinkbyit') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Venom:LostVenom@venom.bopprqu.mongodb.net/?retryWrites=true&w=majority&appName=Venom")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6204193689")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001956404845')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/28a6eaa080f619c8d55cf.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
