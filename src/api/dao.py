from .models import Task
from .schemas import TaskCreate, TaskUpdate

from ..dao import BaseDAO


class TaskDAO(BaseDAO[Task, TaskCreate, TaskUpdate]):
    model = Task