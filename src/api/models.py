from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Task(Base):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=False, nullable=False)
    title: Mapped[str] = mapped_column(unique=False, nullable=False)
    description: Mapped[str] = mapped_column()
    is_finished: Mapped[bool] = mapped_column(default=False)
    
