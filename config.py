import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5097607168:AAGy70RYAiXz2f-YrC8DC1mgZlvdEsCCv20")

    APP_ID = int(os.environ.get("APP_ID", "3119488e-c797-4324-ae1e-61e4d12a0a8b"))

    API_HASH = os.environ.get("API_HASH", "120.29.108.14")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Kai84_Space")
