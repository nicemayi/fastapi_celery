from celery import Celery
from products.tasks import update_product_from_api

# Use Redis as both broker and backend storage
app = Celery('celery_tasks', backend='redis://redis',
             broker='redis://redis')  # use redis name from docker
app.conf.timezone = 'US/Pacific'


@app.task
def task_update_product(url, payload):
    return update_product_from_api(url, payload)
