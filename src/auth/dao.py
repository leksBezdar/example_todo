from .models import User
from .schemas import UserCreateDB, UserUpdate

from ..dao import BaseDAO


class UserDAO(BaseDAO[User, UserCreateDB, UserUpdate]):
    model = User
