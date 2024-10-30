from steam_web_api import Steam
from app.core.config import settings
steam = Steam(settings.STEAM_WEB_API_KEY)


def friends(user_id):
    user = steam.users.get_user_friends_list(user_id)
    return user


