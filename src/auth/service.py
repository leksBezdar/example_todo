from fastapi.responses import JSONResponse

from sqlalchemy import or_
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, exceptions, schemas, utils

from .dao import UserDAO
from .models import User

from ..utils import get_unique_id


class UserCRUD:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: schemas.UserCreate) -> models.User:

        if await self.get_existing_user(username=user.username, email=user.email):
            raise exceptions.UserAlreadyExists

        id = await get_unique_id()

        hashed_password = await utils.get_hashed_password(user.password)

        # Создание экземпляра User с предоставленными данными
        db_user = await UserDAO.add(
            self.db,
            schemas.UserCreateDB(
                **user.model_dump(),
                id=id,
                hashed_password=hashed_password
            )
        )

        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)

        return db_user

    async def authenticate_user(self, username: str, password: str) -> User:

        try:
            user = await self.get_existing_user(username=username)
            await utils.validate_password(password=password, hashed_password=user.hashed_password)

            return user

        except AttributeError:
            raise exceptions.InvalidAuthenthicationCredential

    async def get_existing_user(self, email: str = None, username: str = None, user_id: str = None) -> User:

        if not email and not username and not user_id:
            raise exceptions.NoUserData

        user = await UserDAO.find_one_or_none(self.db, or_(
            User.email == email,
            User.username == username,
            User.id == user_id))

        return user

    # Получение списка всех пользователей с поддержкой пагинации

    async def get_all_users(self, *filter, offset: int = 0, limit: int = 100, **filter_by) -> list[User]:

        users = await UserDAO.find_all(self.db, *filter, offset=offset, limit=limit, **filter_by)

        return users

    async def delete_user(self, user_id: str = None) -> str:

        if not user_id:
            raise exceptions.NoUserData

        user = await self.get_existing_user(user_id=user_id)

        if not user:
            raise exceptions.UserDoesNotExist

        await UserDAO.delete(self.db, user_id == User.id)

        await self.db.commit()

        return {"Message": "Delete was successful"}


class DatabaseManager:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_crud = UserCRUD(db)

    # Применение изменений к базе данных
    async def commit(self):
        await self.db.commit()