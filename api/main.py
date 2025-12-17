from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.get("/api/")
def root():
    r.incr("hits")
    return {"message": "Hello from FastAPI", "hits": r.get("hits")}

