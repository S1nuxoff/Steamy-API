from steam_web_api import Steam
from app.core.config import settings
steam = Steam(settings.STEAM_WEB_API_KEY)


def badges(user_id):
    user = steam.users.get_user_badges(user_id)
    return user


