from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str 
    username: str 
    description: str 
    is_finished: bool = False
    

class Task(TaskBase):
    id: int
    
    
class TaskCreate(TaskBase):
    pass

# Схема для обновления записи (CRUD - Update)
class TaskUpdate(BaseModel):
    title: str | None = None
    username: str | None = None
    description: str | None = None
    is_finished: bool | None = None
