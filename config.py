from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e8056a9683ca6fbe1780f.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/ccbd014af4ceeb890c168.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/rev_fxx")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/def_Zoka")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6094482545").split()))


FAILED = "https://telegra.ph/file/5b27a3f1f746a8638fe31.jpg"
