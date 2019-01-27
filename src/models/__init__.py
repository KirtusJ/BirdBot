from .model import database
from .discord_users import DiscordUser

database.Base.metadata.create_all(database.engine)
