# @Owner_of_qtmve

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID","22939818"))
    API_HASH = str(environ.get("API_HASH","ef43fe3762fb69770897433112183da3"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "6890961089:AAFkn2F5VEihe7MH8I95n5GdhZ1w8D87QPk"))
    SHORTNER_API = str(environ.get("SHORTNER_API", "02c93c55c4567035a37ffc32731d8f0e1c530f98")) 
    SHORTENR_URL = str(environ.get("SHORTENR_URL", "tnshort.net")) 
    AUTH_CHANNEL = str(environ.get("AUTH_CHANNEL", "Qtmve_linkZzz")) 
    CUSTOM_FILE_CAPTION = str(environ.get("CUSTOM_FILE_CAPTION","<b><i>{file_name}\n\n⚡️ 𝐅𝐚𝐬𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 : \n{short_link}\n\n𝐉𝐨𝐢𝐧 -⋙ @{main_chat} </i></b>")) 
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1002124854329"))  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1600"))  # 20 minutes
    HAS_SSL = environ.get("HAS_SSL", False)
    HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
    NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = True if str(NO_PORT).lower() == "true" else False
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(environ.get("APP_NAME"))
    else:
        ON_HEROKU = False
    FQDN = (
        str(environ.get("FQDN", BIND_ADDRESS))
        if not ON_HEROKU or environ.get("FQDN")
        else APP_NAME + ".herokuapp.com"
    )
    if ON_HEROKU:
        URL = f"https://{FQDN}/"
    else:
        URL = f"{FQDN}/"

    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "aredirect"))
    OWNER_ID = int(environ.get('OWNER_ID', '5485563713'))

    BANNED_CHANNELS = list(set(int(x) for x in str(environ.get("BANNED_CHANNELS", "-1001296894100")).split()))
