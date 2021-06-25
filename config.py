import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", ""))

    API_HASH = os.environ.get("API_HASH", "")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Kai84_Space")


    UPDATES_CHANNEL_2 = os.environ.get("UPDATES_CHANNEL_2", "Anime_Troop")
    

    UPDATES_CHANNEL_3 = os.environ.get("UPDATES_CHANNEL_3", "Movie_Bank")
