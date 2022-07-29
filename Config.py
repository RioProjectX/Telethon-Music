import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19601567"))
    API_HASH = os.environ.get("API_HASH", "c837bfe31d4b532dc84eb38d62a0c4bd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5109381626:AAH0cosvoJrmSOBx1I2E1i3aPuOojkGd-xI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@MircMusicbot")
    SUPPORT = os.environ.get("SUPPORT", "MCMusicz")
    CHANNEL = os.environ.get("CHANNEL", "MCMusicz")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/5b39746a9cbb3b7273c3a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2"))
