import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "5783157101:AAGQ_EpmpYFKWCrlGqQsyoFqbw1M3CuTVmA") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 10956858)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "cceefd3382b44d4d85be2d83201102b7") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 5412376600)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

    LOG_CHANNAL = -1001565287482
