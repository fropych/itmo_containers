import os
from fastapi import FastAPI
import redis

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/")
def read_root():
    count = r.incr("hits")
    return {"message": "Hello from Docker Compose!", "hits": count}

@app.get("/health")
def health_check():
    try:
        if r.ping():
            return {"status": "ok", "redis": "connected"}
    except redis.ConnectionError:
        return {"status": "error", "redis": "disconnected"}
