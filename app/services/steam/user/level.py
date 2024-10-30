from steam_web_api import Steam
from app.core.config import settings
steam = Steam(settings.STEAM_WEB_API_KEY)

def level(user_id):
    user = steam.users.get_user_steam_level(user_id)
    return user


