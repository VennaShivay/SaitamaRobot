# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os



def get_user_list(config, key):
    with open("{}/SaitamaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 22743513  # integer value, dont use ""
    API_HASH = "38f450dee835a7668fbaec9655ebcca8"
    TOKEN = "5661136581:AAG_-rajn2TVRqvRKEQvZ7s3XZ7slHb3Phw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "1493545483"  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Pilotgalaxy"
    SUPPORT_CHAT = "SpicySupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001892869506
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001867640248
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ALLOW_CHATS = True

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://astra309:aFSGIFcpuzaurhOf8MdpfRlAzTeyvqN5@dpg-cgok668u9tun42pfn5hg-a.oregon-postgres.render.com/astra"  # needed for any database modules
    DB_NAME = "astra"  # needed for cron_jobs module, use same databasename from SQLALCHEMY_DATABASE_URI
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = https://i.imgur.com/2U2SbFp.jpeg
    SPAMWATCH_API = "VNQHaQdcjVqhdk4~CjUQStHzwsK3kFu4sv3cxkanmQAGRkELOfKNDQHQ6vc0cfE3"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    WEATHER_API = "0f70542f581639c3737e62b8e22f2761"  # go to openweathermap.org/api to get key

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    SUPPORT_USERS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgIAAxkBAAEHISFjtp1KblH7B3ccqaN_gOb1OBuwrQAC0RMAAgTpQEl0MayeQbPCUi0E"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "VWJBW51U8UZ8"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "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"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    
    BACKUP_PASS = "12345" # The password used for the cron backups zip
    DROP_UPDATES = False # whether to drop the pending updates or not

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
    
