from typing import Any, Dict

from fastapi import FastAPI
from pydantic import BaseModel
from celery_tasks import task_update_product


# Default delay 15 seconds
DEFAULT_DELAY = 15
app = FastAPI()


class Task(BaseModel):
    post_url: str
    delay: int = DEFAULT_DELAY
    description: str = None
    payload: Dict[Any, Any]


@app.get('/')
def greeting():
    return {'Hello'
            'World!'}


@app.post('/tasks/')
async def product_task(task: Task):
    # For demo purpose
    # repeat the job 10 times
    # Note: In production meaning this will trigger 10
    # requests immediately after delay seconds
    for _ in range(1):
        task_update_product.apply_async(
            (task.post_url, task.payload,),
            countdown=task.delay,
        )
    return {'message': 'Send jobs!'}
