from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "24025974"))
    API_HASH = getenv("API_HASH", "2abf0406f41a57b540bdefe8b12d114f")
    BOT_TOKEN = getenv("BOT_TOKEN", "6615313068:AAGcPqcI4BxCw2ksGUGA1qkibkQJ_OMUN-w")
    FSUB = getenv("FSUB", "PanindiaFilmZ")
    CHID = int(getenv("CHID", "-1001930424346"))
    SUDO = list(map(int, getenv("SUDO", "5549620776").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://vasanthtg8:vasanthtg8@cluster0.441zwwt.mongodb.net/?retryWrites=true&w=majority")
cfg = Config()
