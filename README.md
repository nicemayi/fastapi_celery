### Installation

#### Virtualenv
```
python -m venv virtualenv
source virtualenv/bin/activate # deactivate
pip install -r requirements.txt
```

#### Redis
For maOS uses Redis server from Docker, and install redis-client manually
```
docker run --name dev-redis -p 6379:6379 -d redis

# client
brew install redis
# test
redis-cli -h localhost -p 6379 ping
# pong
```

### Start
3 terminals

For Celery worker:
```
celery -A celery_tasks worker --loglevel=INFO
```

For Celery Flower:
```
celery -A celery_tasks flower --address=localhost --port=5566
```

For FastAPI server:
```
uvicorn main:app --reload
```

### Play!
FastAPI comes with swagger for free: http://localhost:5566/tasks
Try add the following payload to http://127.0.0.1:8000/docs#/default/product_task_tasks__post:
```
{
    "post_url": "https://dummyjson.com/products/1",
    "delay": 20,
    "payload": {
        "title": "iPhone Galaxy +1"
    }
}
```
Then cehck from Flower UI: http://localhost:5566/tasks

Note: For testing purpose https://dummyjson.com/products/1 just a free/fake web api.
