from steam_web_api import Steam
from app.core.config import settings
steam = Steam(settings.STEAM_WEB_API_KEY)


def achievements(user_id, app_id):
    user = steam.apps.get_user_achievements(user_id, app_id)
    return user


