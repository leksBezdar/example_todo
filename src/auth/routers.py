from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas

from .models import User
from .service import DatabaseManager
from ..database import get_async_session


router = APIRouter()


@router.post("/registration/", response_model=schemas.User)
async def create_user(
    user_data: schemas.UserCreate,
    db: AsyncSession = Depends(get_async_session),
) -> schemas.User:

    db_manager = DatabaseManager(db)
    user_crud = db_manager.user_crud

    return await user_crud.create_user(user=user_data)


@router.post("/login/", response_model=schemas.User)
async def login(
    username: str,
    password: str,
    db: AsyncSession = Depends(get_async_session),
) -> schemas.User:
    db_manager = DatabaseManager(db)
    user_crud = db_manager.user_crud

    user = await user_crud.authenticate_user(username=username, password=password)

    return user


@router.get("/get_user", response_model=schemas.User)
async def get_user(
    user_id: str = None,
    db: AsyncSession = Depends(get_async_session),
) -> schemas.User | None:

    db_manager = DatabaseManager(db)
    user_crud = db_manager.user_crud

    user = await user_crud.get_existing_user(user_id=user_id)

    return user


@router.get("/get_all_users", response_model=list[schemas.User])
async def get_all_users(
    offset: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session),
) -> list[schemas.User]:
    db_manager = DatabaseManager(db)
    user_crud = db_manager.user_crud

    return await user_crud.get_all_users(offset=offset, limit=limit)


@router.delete("/delete_user")
async def delete_user(
    user_id: str = None,
    db: AsyncSession = Depends(get_async_session),
) -> dict:

    db_manager = DatabaseManager(db)
    user_crud = db_manager.user_crud

    response = await user_crud.delete_user(user_id=user_id)

    return response