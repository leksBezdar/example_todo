from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy.sql import func

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    is_superuser: Mapped[bool] = mapped_column(nullable=False, default=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
