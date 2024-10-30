from fastapi import APIRouter, Depends, HTTPException, status

from app.services.steam.user.search import search
from app.services.steam.user.stats import stats
from app.services.steam.user.wishlist import wishlist
from app.services.steam.user.bans import bans
from app.services.steam.user.badges import badges
from app.services.steam.user.recently_played_games import recently_played_games
from app.services.steam.user.friends import friends
from app.services.steam.user.details import details
from app.services.steam.user.level import level
from app.services.steam.user.achievements import achievements
from app.services.steam.user.owned_games import owned_games

router = APIRouter()

@router.get("/search")
async def search_endpoint(steam_id:int):
    data = search(steam_id)
    return data


@router.get("/stats")
async def stats_endpoint(steam_id:int, appid:int):
    data = stats(steam_id, appid)
    return data

@router.get("/wishlist")
async def wishlist_endpoint(steam_id:int):
    data = wishlist(steam_id)
    return data

@router.get("/bans")
async def bans_endpoint(steam_id:int):
    data = bans(steam_id)
    return data

@router.get("/badges")
async def badges_endpoint(steam_id:int):
    data = badges(steam_id)
    return data

@router.get("/recently_played_games")
async def recently_played_games_endpoint(steam_id:int):
    data = recently_played_games(steam_id)
    return data

@router.get("/friends")
async def friends_endpoint(steam_id:int):
    data = friends(steam_id)
    return data

@router.get("/details")
async def details_endpoint(steam_id:int):
    data = details(steam_id)
    return data

@router.get("/level")
async def level_endpoint(steam_id:int):
    data = level(steam_id)
    return data

@router.get("/achievements")
async def achievements_endpoint(steam_id:int):
    data = achievements(steam_id)
    return data

@router.get("/owned_games")
async def owned_games_endpoint(steam_id:int):
    data = owned_games(steam_id)
    return data
