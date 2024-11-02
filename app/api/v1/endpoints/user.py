from typing import Optional

from fastapi import APIRouter, Depends

from app.api import deps
from app.exceptions.custom_exceptions import UserAlreadyExistsException, UserNotFoundException
from app.schemas.user import User, UserCreate, UserUpdate, UserAddFavorite, UserRemoveFavorite
from app.schemas.favourite import FavouriteResponse

from app.services.user.get_by_id import get_user_by_id
from app.services.user.create import create_user
from app.services.user.update import update
from app.services.user.add_favourite import add_favorite
from app.services.user.remove_favorite import remove_favorite
from app.services.user.get_favorites import get_favorites

router = APIRouter()


# GET--------------------------------------------------------------------------------------------------------------------
@router.get("/", response_model=User, summary="Get user by telegram id")
async def get_user_endpoint(tg_id: int, current_user: User = Depends(deps.get_current_user)):
    user = await get_user_by_id(tg_id)
    if not user:
        raise UserNotFoundException()
    return user

@router.get("/favorites", summary="Update user")
async def get_user_favorite_endpoint(
        tg_id: int,
        game: Optional[str] = None,
        current_user: User = Depends(deps.get_current_user)
):
    user = await get_user_by_id(tg_id)
    if not user:
        raise UserNotFoundException()
    favorites = await get_favorites(user, game)
    return favorites

# GET--------------------------------------------------------------------------------------------------------------------

# POST-------------------------------------------------------------------------------------------------------------------
@router.post("/create", response_model=User, summary="Create new user")
async def create_new_user_endpoint(user_in: UserCreate, current_user: User = Depends(deps.get_current_user)):
    existing_user = await get_user_by_id(user_in.tg_id)
    if existing_user:
        raise UserAlreadyExistsException()
    user = await create_user(user_in)
    return user


# POST-------------------------------------------------------------------------------------------------------------------

# PATCH------------------------------------------------------------------------------------------------------------------
@router.patch("/update", response_model=User, summary="Update user")
async def update_user_endpoint(
        tg_id: int,
        user_in: UserUpdate,
        current_user: User = Depends(deps.get_current_user)
):
    user = await get_user_by_id(tg_id)
    if not user:
        raise UserNotFoundException()
    user = await update(user, user_in)
    return user


@router.patch("/add_favorite", response_model=FavouriteResponse, summary="Update user")
async def add_user_favorite_endpoint(
        tg_id: int,
        user_in: UserAddFavorite,
        current_user: User = Depends(deps.get_current_user)
):
    user = await get_user_by_id(tg_id)
    if not user:
        raise UserNotFoundException()
    new_favorite = await add_favorite(user, user_in)
    return new_favorite


# PATCH------------------------------------------------------------------------------------------------------------------

# DELETE-----------------------------------------------------------------------------------------------------------------
@router.delete("/remove_favorite", response_model=FavouriteResponse, summary="Update user")
async def add_user_favorite_endpoint(
        tg_id: int,
        user_in: UserRemoveFavorite,
        current_user: User = Depends(deps.get_current_user)
):
    user = await get_user_by_id(tg_id)
    if not user:
        raise UserNotFoundException()
    removed_favorite = await remove_favorite(user, user_in)
    return removed_favorite
# DELETE-----------------------------------------------------------------------------------------------------------------
