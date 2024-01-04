from sqlalchemy.ext.asyncio import AsyncSession


from . import schemas

from .dao import TaskDAO
from .models import Task


class TaskCRUD:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_task(self, task: schemas.TaskCreate) -> Task:
        
        if not task: 
            return {"Error_message": "Task data is required"}
        
        db_task = await TaskDAO.add(
            self.db,
            schemas.TaskCreate(
                **task.model_dump(),
            )
        )

        self.db.add(db_task)
        await self.db.commit()
        await self.db.refresh(db_task)

        return db_task
    
    async def get_task(self, task_id: int) -> Task:
        
        if not task_id:
            return {"Error_message": "task_id is required"}
        
        task = await TaskDAO.find_one_or_none(self.db, Task.id == task_id)
        
        return task
        
    async def get_all_tasks(self, limit, offset) -> list[Task]:
        
        tasks = await TaskDAO.find_all(self.db, offset=offset, limit=limit)
        
        return tasks
    
    async def update_task(self, task_id: int, task_in: schemas.TaskUpdate) -> Task:
        
        task_update = await TaskDAO.update(
            self.db,
            Task.id == task_id,
            obj_in=task_in)

        await self.db.commit()

        return task_update
    
    async def delete_task(self, task_id: int = None) -> str:
        
        if not task_id:
            return {"Error_message": "task_id is required"}
        
        
        await TaskDAO.delete(self.db, task_id == Task.id)

        await self.db.commit()
        
        return {"Message": f"task {task_id} was deleted successfully"}
    
    
class TaskManager:
    
    def __init__(self, db: AsyncSession):
        self.db = db 
        self.task_crud = TaskCRUD(db)