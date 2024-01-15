from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas
from .models import Task
from .service import TaskManager

from ..database import get_async_session


router = APIRouter()


@router.post("/create_task/", response_model=schemas.TaskBase)
async def create_task(
    task_data: schemas.TaskCreate,
    db: AsyncSession = Depends(get_async_session),
) -> Task:

    db_manager = TaskManager(db)
    task_crud = db_manager.task_crud

    return await task_crud.create_task(task=task_data)


@router.get("/get_task/", response_model=schemas.TaskBase)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_async_session),
) -> Task:

    db_manager = TaskManager(db)
    task_crud = db_manager.task_crud

    return await task_crud.get_task(task_id)


@router.get("/get_all_tasks")
async def get_all_tasks(
    limit: int = 10,
    offset: int = 0,
    db: AsyncSession = Depends(get_async_session),
) -> list[schemas.TaskBase]:

    db_manager = TaskManager(db)
    task_crud = db_manager.task_crud

    return await task_crud.get_all_tasks(limit, offset)


@router.patch("/update_task")
async def update_task(
    task_id: int, 
    task_data: schemas.TaskUpdate,
    db: AsyncSession = Depends(get_async_session),
) -> schemas.TaskBase:

    db_manager = TaskManager(db)
    task_crud = db_manager.task_crud

    return await task_crud.update_task(task_id, task_in=task_data)


@router.delete("/delete_task")
async def delete_task(
    task_id: int, 
    db: AsyncSession = Depends(get_async_session),
):

    db_manager = TaskManager(db)
    task_crud = db_manager.task_crud

    return await task_crud.delete_task(task_id)