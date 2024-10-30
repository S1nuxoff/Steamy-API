from steam_web_api import Steam
from app.core.config import settings
steam = Steam(settings.STEAM_WEB_API_KEY)
import asyncio

def search(user_id):
    user = steam.users.search_user(user_id)
    return user

