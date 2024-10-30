from steam_web_api import Steam
from app.core.config import settings
steam = Steam(settings.STEAM_WEB_API_KEY)


def wishlist(user_id):
    user = steam.users.get_profile_wishlist(user_id)
    return user


